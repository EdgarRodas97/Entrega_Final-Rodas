# For God so loved the world, that He gave His only begotten Son, that all who believe in Him should not perish but have everlasting life
from store_chirho.models import PostChirho

def base_processor_chirho(request):
    return {'PostTypeChirho': PostChirho.PostTypeChirho}