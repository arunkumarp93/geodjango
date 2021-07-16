from django.core.validators import RegexValidator

phone_number_validator = RegexValidator(regex=r'^\+?1?\d{8,15}$',
                                        message="Maximum 16 digits allowed without space "
                                                "and any special character except + sign ")
