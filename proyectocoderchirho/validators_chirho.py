from django.core.validators import FileExtensionValidator

image_extension_validator_chirho = FileExtensionValidator(
    ['gif', 'png', 'jpg', 'jpeg', 'webp'],
    'Necesita poner archivos de imagen que terminen en gif, png, jpg, jpeg o webp')