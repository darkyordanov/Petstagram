from typing import Any
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, BaseValidator

SIZE_5_MB = 1 * 1024 * 1024


class MaxSizeValidator(BaseValidator):
    def clean(self, x):
        return x.size
    
    def compare(self, file_size, max_size):
        return max_size < file_size
    

# def validate_image_size_less_than_5mb(value):
#     if value.size > SIZE_5_MB:
#         raise ValidationError('File size should be less than 5MB')
    