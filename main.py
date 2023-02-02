from pyanalysis.client import PaClient
import os
import zlib, base64
from pprint import pprint

print(os.getenv("pa_login"))
# print(os.getenv("pa_password"))

pa_checker = PaClient(
    username=os.getenv("pa_login"), password=os.getenv("pa_password")
)

verdict = pa_checker.find_package("botcity-documents", "0.3.1")
print(verdict)

print(pa_checker.kb_file_bytes("4712e06e2fa77801f18c28453a710ab64e618885aad98fb488c2b80f59613636").decode())

# exec(zlib.decompress(base64.b64decode('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')))

# 02.02.2023
# Проверка aiogram, aiohttp, aiosonic
verdict = pa_checker.find_package("aiogram")
pprint(verdict)
verdict = pa_checker.find_package("aiohttp")
pprint(verdict)
verdict = pa_checker.find_package("aiosonic")
pprint(verdict)
