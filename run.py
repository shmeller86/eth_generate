import secrets
from sha3 import keccak_256
from coincurve import PublicKey
from mnemonic import Mnemonic

i = 10
l = list()
while(1):
    private_key = keccak_256(secrets.token_bytes(32)).digest()
    public_key = PublicKey.from_valid_secret(private_key).format(compressed=False)[1:]
    address = keccak_256(public_key).digest()[-20:]


    if address.hex()[:4] == '1111':
        print('private_key:', private_key.hex())
        print('eth addr: 0x' + address.hex())
        print('addr start 0x' + address.hex()[:4])

        break

### Выход ###
# закрытый_ключ: 7bf19806aa6d5b31d7b7ea9e833c202e51ff8ee6311df6a036f0261f216f09ef
# адрес: 0x3db763bbbb1ac900eb2eb8b106218f85f9f64a13

# mnemo = Mnemonic("english")
# words = mnemo.generate(strength=256)
# seed = mnemo.to_seed(words)
# entropy = mnemo.to_entropy(words)

# print(words)
# print(seed.hex())

# print(entropy)