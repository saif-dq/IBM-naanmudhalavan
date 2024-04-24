import re

class EmailValidator:
    def __init__(self):
        self.safe_domains = ["gmail.com", "yahoo.com", "outlook.com"]  # Example safe domains

    def validate_email(self, email):
        # Check if email format is valid
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            print("Invalid email format!")
            return False

        # Check if domain is safe
        domain = email.split('@')[1]
        if domain not in self.safe_domains:
            print("Unsafe email domain detected!")
            return False

        print("Email validation successful.")
        return True

class PhishingDetector:
    def __init__(self):
        self.known_phishing_domains = ["phishingsite.com", "scammer.org"]  # Example known phishing domains

    def detect_phishing(self, email):
        domain = email.split('@')[1]
        if domain in self.known_phishing_domains:
            print("Phishing domain detected!")
            return True

        print("Email appears to be safe.")
        return False

# Example usage
if __name__ == "__main__":
    email_validator = EmailValidator()
    phishing_detector = PhishingDetector()

    # Validate email
    email = "user@example.com"
    if email_validator.validate_email(email):
        # Check for phishing
        phishing_detector.detect_phishing(email)
