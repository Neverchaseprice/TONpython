# TONpython
TON with Python 


# Задача 1: Сделать ТОН-кошелек на TestNet и задеплоить его
Сначала Блок теории, потом блок практики


# Теория




# Практика
Создадим файл "wallet_creation"
Создадим Кошелек на Тест-нет с помощью библиотеки Ton SDK и методов

from tonsdk.contract.wallet import Wallets, WalletVersionEnum
import mnemonics_data
mnemonics = mnemonics_data.wallet_test_1
mnemonics, pub_k, priv_k, wallet = Wallets.from_mnemonics(mnemonics=mnemonics, version=WalletVersionEnum.v3r2, workchain=0)

Метод Wallets.create возвращает 4 метрики:
Мнемонику (mnemonics), это seed-фраза
Публичный ключ (pub_k),
Приватный ключ (priv_k),
Адрес Кошелька (wallet)
Wallet - это объект класса


Создадим отдельный файл для хранения "секретных" переменных. Создадим файл "mnemonics_data.py" и поместим mnemomics (seed-фразу) в переменную wallet_test_1 

В файле "mnemonics_data.py"
wallet_test_1 = ['word1', 'word2, ...., word12]

Вернемся к файлу "wallet_creation", в нем осталось только выполнить код

if __name__ == '__main__':
    print(mnemonics)
    print((wallet.address.to_string(True, True, True, True)))

Если написать просто print((wallet.address.to_string())), то будет выведен адрес в 16-ричной форме (формат HEX).
Поэтому нам надо прописать print((wallet.address.to_string(True, True, True,True)))
Мы пишем 4 True, так как мы работаем с Тестнетом и четвертое "True" дает кошелек в Test-Net форме.
Мы сначала создали кошелек через "Wallets.create(version=WalletVersionEnum.v3r2, workchain=0)"

Итого весь файл выглядит: 

from tonsdk.contract.wallet import Wallets, WalletVersionEnum
import mnemonics_data
mnemonics = mnemonics_data.wallet_test_1
mnemonics, pub_k, priv_k, wallet = Wallets.from_mnemonics(mnemonics=mnemonics, version=WalletVersionEnum.v3r2, workchain=0)

if __name__ == '__main__':
    print(mnemonics)
    print((wallet.address.to_string(True, True, True, True)))
    
 
