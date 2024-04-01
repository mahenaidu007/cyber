import hashlib

def hide_text_in_hash(text, secret_message):
    hash_value = hashlib.sha256(text.encode()).hexdigest()
    return hash_value + secret_message

def extract_text_from_hash(hidden_text):
    hash_length = 64  # SHA-256 hash length
    hash_value = hidden_text[:hash_length]
    secret_message = hidden_text[hash_length:]
    return hash_value, secret_message

# Example Usage
original_text = "Hello, this is a secret message."
hidden_text = hide_text_in_hash(original_text, " Don't tell anyone!")
print("Hidden Text:", hidden_text)

hash_value, extracted_message = extract_text_from_hash(hidden_text)
print("Extracted Message:", extracted_message)
