# TONpython
TON with Python 


# Задача 1: Сделать ТОН-кошелек на TestNet и задеплоить его
Сначала Блок теории, потом блок практики


# Теория
Смарт-контракты TON пишутся на языке FunC и Fift, а исполняются на виртуальной машине TON (Telegram Open Network Virtual Machine).

Для взаимодействия с блокчейном необходим установить и использовать lite-client (гайд по его установке), само взаимодействие происходит по API и SDK.

Полезные приложения и инструменты:
Плагины для редакторов кода — IDEA, Sublime Text, VS Code.
Бесплатный HTTP API — Toncenter.
Инструментарий для разработки смарт-контрактов — toncli.
Каталог приложений и инструментов — Ton App.
Можно запускать локальный блокчейн прямо на компьютере через MyLocalTON, либо использовать тестовую сеть.

Материал для изучения:

Библиотека для разработчиков TON.
Основные рекомендации по смарт-контрактам.
Пошаговый пример развертывания смарт контракта.
Статья о том как написать и опубликовать смарт-контракт в TON.
Ton NFT white paper.

В качестве примеров или основы смарт контрактов можно использовать репозитории с github.com:

Смарт контракты.
Смарт контракты ton whales.
Контракт простого кошелька.

Сообщества разработчиков вокруг TON:

Основное русскоязычное.
Неофициальное о разработке смарт-контрактов.
Tonic.





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
    
 
