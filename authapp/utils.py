# library
from django.contrib.auth.tokens import PasswordResetTokenGenerator
import six
class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self,user,timestamp):
        return (six.text_type(user.pk)+six.text_type(timestamp)+six.text_type(user.is_active))
generate_token=TokenGenerator()

def calculate_bmi(height_cm, weight_kg):
    """Calculates BMI given height (in cm) and weight (in kg)"""
    height_m = height_cm / 100.0
    bmi = weight_kg / (height_m ** 2)
    return round(bmi, 2)