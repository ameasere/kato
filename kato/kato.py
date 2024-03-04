import sentry_sdk
from sentry_sdk.integrations.starlette import StarletteIntegration
from sentry_sdk.integrations.fastapi import FastApiIntegration
from sentry_sdk.integrations.asyncio import AsyncioIntegration
import requests
import os
secrets = requests.get('https://api.doppler.com/v3/configs/config/secrets/download?project=kato&config=prd&format=json&include_dynamic_secrets=false', headers={"Accept": "application/json", "Authorization": f"Bearer {os.environ['DOPPLER_TOKEN_KATO']}"}).json()
sentry_dsn = secrets["SENTRY_DSN"]
sentry_sdk.init(
    dsn=sentry_dsn,
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    traces_sample_rate=1.0,
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.
    profiles_sample_rate=1.0,
    enable_tracing=True,
)


class Kato:
    def __init__(self, key):
        self.key = key
        self.key_length = len(key)
        self.s_box = [

        ]
        self.inv_s_box = [

        ]
        self.r_con = [

        ]
        self.mix_columns = [

        ]
        self.inv_mix_columns = [

        ]
        self.rounds = 14
        self.block_size = 16

    def analyze(self, func, *args, **kwargs):
        with sentry_sdk.start_transaction(op="analyze", name=func.__name__):
            return func(*args, **kwargs)

    def encrypt(self, plaintext):
        pass

    def decrypt(self, ciphertext):
        pass
