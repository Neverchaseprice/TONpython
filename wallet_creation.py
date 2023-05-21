#Создадим Кошелек на Тест-нет с помощью библиотеки Ton SDK и методов

from tonsdk.contract.wallet import Wallets, WalletVersionEnum

mnemonics = ['three', 'pen', 'gasp', 'own', 'bar', 'ship', 'absent', 'spider', 'identify', 'ozone', 'dial', 'salon', 'useful', 'fly', 'fantasy', 'scrap', 'sustain', 'during', 'inner', 'oval', 'west', 'story', 'provide', 'maximum']
mnemonics, pub_k, priv_k, wallet = Wallets.from_mnemonics(mnemonics=mnemonics, version=WalletVersionEnum.v3r2, workchain=0)

#Метод Wallets.create возвращает 4 метрики:
# Мнемонику (mnemonics),
# Публичный ключ (pub_k),
# Приватный ключ (priv_k),
# Адрес Кошелька (wallet)

#Wallet - это объект класса

if __name__ == '__main__':
    print(mnemonics)
    print((wallet.address.to_string(True, True, True, True)))

#Если написать просто print((wallet.address.to_string())), то будет выведен адрес в 16-ричной форме (формат HEX).
# Поэтому нам надо прописать print((wallet.address.to_string(True, True, True,True)))
# Мы пишем 4 True, так как мы работаем с Тестнетом и четвертое "True" дает кошелек в Test-Net форме.

#Мы сначала создали кошелек через "Wallets.create(version=WalletVersionEnum.v3r2, workchain=0)"
#['three', 'pen', 'gasp', 'own', 'bar', 'ship', 'absent', 'spider', 'identify', 'ozone', 'dial', 'salon', 'useful', 'fly', 'fantasy', 'scrap', 'sustain', 'during', 'inner', 'oval', 'west', 'story', 'provide', 'maximum']
#kQB6hJB0r97Rm-w5HRE0JZ90LEHqhibA0tgXQozX7xZbSaYa

#https://testnet.tonscan.org/address/EQB6hJB0r97Rm-w5HRE0JZ90LEHqhibA0tgXQozX7xZbSR2Q#transactions