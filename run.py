import secrets
from sha3 import keccak_256
from coincurve import PublicKey

private_key = keccak_256(secrets.token_bytes(32)).digest()
public_key = PublicKey.from_valid_secret(private_key).format(compressed=False)[1:]
address = keccak_256(public_key).digest()[-20:]

print('private_key:', private_key.hex())
print('eth addr: 0x' + address.hex())