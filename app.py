from flask import Flask, render_template, request
from password_strength import analyze_password
import logging

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'  # Replace with secure key in production

# ===================
# Logging Configuration
# ===================
logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# ===================
# Routes
# ===================
@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    error = None
    password = ""

    try:
        if request.method == 'POST':
            password = request.form.get('password', '').strip()

            if not password:
                raise ValueError("Password cannot be empty.")

            result = analyze_password(password)

            if result.get('error'):
                logging.warning(f"[Analyzer Warning] {result.get('message')}")
                raise Exception(result.get('message'))

            logging.info("Password analyzed successfully.")

    except ValueError as ve:
        logging.warning(f"[Input Error] {str(ve)}")
        error = str(ve)

    except Exception as e:
        logging.error(f"[Unexpected Error] {str(e)}")
        error = "An error occurred during password analysis. Please try again."

    return render_template(
        'index.html',
        result=result,
        password=password,
        error=error
    )

# ===================
# Entry Point
# ===================
if __name__ == '__main__':
    print("⚡ Starting Flask App...")
    app.run(debug=True, use_reloader=False)


