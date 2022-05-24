Although Python is not the best choice for this task due to the slow interpreter, I will analyze the generation on it.

For the current task from the modules, we need:
coincurve - Cross platform python CFFI bindings for libsecp256k1
pysha3 - SHA-3 wrapper for python (with keccak support)

Address generation in the Ethereum network occurs in 3 stages:
1. Private key generation
2. Obtaining a public key from a private one
3. Getting the address from the public key

You need to understand that the public key and the Etherium address are different things. Addresses are hashes of public keys and it is not possible to send funds to a public key.

Original article https://4trading.app/python/generacziya-ethereum-adresov-na-python/