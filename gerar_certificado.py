import ipaddress
import datetime
from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa

chave_privada = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)

nome = x509.Name([
    x509.NameAttribute(NameOID.COMMON_NAME, u"CapSendFlow Local"),
])

certificado = (
    x509.CertificateBuilder()
    .subject_name(nome)
    .issuer_name(nome)
    .public_key(chave_privada.public_key())
    .serial_number(x509.random_serial_number())
    .not_valid_before(datetime.datetime.utcnow())
    .not_valid_after(datetime.datetime.utcnow() + datetime.timedelta(days=365))
    .add_extension(
        x509.SubjectAlternativeName([
            x509.IPAddress(ipaddress.IPv4Address(u"192.168.0.8")),
            x509.DNSName(u"localhost"),
        ]),
        critical=False,
    )
    .sign(chave_privada, hashes.SHA256())
)

with open("key.pem", "wb") as arquivo_chave:
    arquivo_chave.write(chave_privada.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption(),
    ))

with open("cert.pem", "wb") as arquivo_certificado:
    arquivo_certificado.write(certificado.public_bytes(serialization.Encoding.PEM))

print("Certificado e chave criados: cert.pem e key.pem")