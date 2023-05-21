#pip3 install pytonlib
#Из библиотеки Pytonlib импортируем TonLibClient
#https://github.com/toncenter/pytonlib

import asyncio
from pytonlib import TonlibClient
import requests
from pathlib import Path
from wallet_creation import wallet
async def main():
    #https://docs.ton.org/develop/smart-contracts/environment/testnet
    #Конфиг передается в виде словаря
    config = requests.get('https://ton.org/testnet-global.config.json').json()

    #https://github.com/toncenter/pytonlib/blob/main/README.md
    # create keystore directory for tonlib
    #keystore_dir = '/ton_keystore_dir/ton_keystore'
    #Path(keystore_dir).mkdir(parents=True, exist_ok=True)
    #C:\Users\1\PycharmProjects\TONPyTON


    client = TonlibClient(ls_index=0, config=config, keystore='C:/tmp/ton_keystore')
    #Конфиг json на официальном сайте
    #KeyStore - это папка для хранения ключа


    await client.init()
    query = wallet.create_init_external_message()

    deploy_message = query['message'].to_boc(False)
          #Метод to_boc отправляет в блокчейн

    await client.raw_send_message(deploy_message)
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

    #https://testnet.tonscan.org/address/EQB6hJB0r97Rm-w5HRE0JZ90LEHqhibA0tgXQozX7xZbSR2Q#transactions