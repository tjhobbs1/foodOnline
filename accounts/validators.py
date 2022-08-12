from django.core.exceptions import ValidationError
import os


def allow_only_images_validator(value):
    ext = os.path.splitext(value.name)[1]
    print(ext)
    valid_extentsions = ['.png', 'jpg', 'jpeg']
    if not ext.lower() in valid_extentsions:
        raise ValidationError(
            "Unsupported File Extension Allowed: " + str(valid_extentsions))
