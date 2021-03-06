from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


# Make sure the crn is valid
def valid_crn(crn):
    if crn < 0 or crn > 100000:
        raise ValidationError(_(f'{crn} is not within the provided bounds'))


# Make sure the section number is valid
def valid_section(section):
    if section < 0 or section > 20:
        raise ValidationError(_(f'{section} is not a valid section number'))
