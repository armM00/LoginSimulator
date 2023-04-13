import hashlib


def encrypt(variable):
    bytes_to_hash = variable.encode("utf-8")
    sha256_hash = hashlib.sha256()
    sha256_hash.update(bytes_to_hash)
    hex_hash = sha256_hash.hexdigest()
    return hex_hash
