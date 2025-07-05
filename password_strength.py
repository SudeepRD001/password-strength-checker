import re
import logging
import unicodedata
from zxcvbn import zxcvbn

# Optional: Add a list of most common passwords (can be extended or read from a file)
COMMON_PASSWORDS = {
    "password", "123456", "qwerty", "letmein", "admin", "welcome", "iloveyou", "abc123"
}

def normalize_input(password: str) -> str:
    """Normalize password input to a consistent Unicode format."""
    return unicodedata.normalize('NFKC', password.strip())

def is_common_password(password: str) -> bool:
    """Check if password is in a known list of common passwords."""
    return password.lower() in COMMON_PASSWORDS

def analyze_password(password: str) -> dict:
    """
    Analyze the strength of a password using zxcvbn and advanced custom rules.
    Returns entropy, crack time, suggestions, and rule compliance.
    """
    try:
        # Input validation
        if not password or not password.strip():
            raise ValueError("Password cannot be empty.")

        password = normalize_input(password)

        if is_common_password(password):
            raise ValueError("This is a very common password. Please choose a more unique one.")

        # Run zxcvbn analysis
        result = zxcvbn(password)

        # Advanced rule checks
        length_ok = len(password) >= 12
        has_upper = bool(re.search(r'[A-Z]', password))
        has_lower = bool(re.search(r'[a-z]', password))
        has_digit = bool(re.search(r'\d', password))
        has_special = bool(re.search(r'[!@#$%^&*(),.?":{}|<>\\[\]~`_\-=+;/]', password))

        rules = {
            'length_ok': length_ok,
            'has_upper': has_upper,
            'has_lower': has_lower,
            'has_digit': has_digit,
            'has_special': has_special,
        }

        passed_all = all(rules.values())

        feedback = result.get('feedback', {})

        # Return structured result
        return {
            "score": result.get('score', 0),
            "crack_time": result.get('crack_times_display', {}).get('offline_fast_hashing_1e10_per_second', 'Unknown'),
            "password_entropy": result.get('entropy', 0.0),
            "password_length": len(password),
            "feedback": feedback,
            "rules": rules,
            "passed_all_rules": passed_all
        }

    except ValueError as ve:
        logging.warning(f"[INPUT ERROR] {str(ve)}")
        return {
            "error": True,
            "message": str(ve)
        }

    except Exception as e:
        logging.exception("[UNEXPECTED ERROR]")
        return {
            "error": True,
            "message": "Password analysis failed due to an unexpected internal error."
        }
