from nucypher.characters import Ursula
from nucypher.crypto.powers import SigningPower


def test_ursula_generates_self_signed_cert(nucypher_test_config):
    ursula = Ursula(attach_server=False, config=nucypher_test_config)
    cert, cert_private_key = ursula.generate_self_signed_certificate()
    public_key_numbers = ursula.public_key(SigningPower).to_cryptography_pubkey().public_numbers()
    assert cert.public_key().public_numbers() == public_key_numbers
