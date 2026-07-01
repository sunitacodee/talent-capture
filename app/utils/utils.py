import random
import string
class Utils:
   
    def generate_verification_code(length=8):
        characters = string.ascii_uppercase + string.digits
        return ''.join(random.choice(characters) for _ in range(length))
