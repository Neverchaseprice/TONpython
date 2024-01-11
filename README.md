# TONpython
TON with Python 


# Задача 1: Сделать 4 ТОН-кошелька на TestNet и задеплоить их

# Теория
Смарт-контракты TON пишутся на языке FunC и Fift, а исполняются на виртуальной машине TON (Telegram Open Network Virtual Machine).
Для взаимодействия с блокчейном необходим установить и использовать lite-client (гайд по его установке), само взаимодействие происходит по API и SDK.

Мнемонику (mnemonics). Это seed-фраза
Публичный ключ (pub_k);
Приватный ключ (priv_k);
Адрес Кошелька (wallet);


# Практика
Создадим файл "wallet_creation"
Создадим Кошелек на Тест-нет с помощью библиотеки Ton SDK и методов

from tonsdk.contract.wallet import Wallets, WalletVersionEnum
import mnemonics_data
mnemonics = mnemonics_data.wallet_test_1
mnemonics, pub_k, priv_k, wallet = Wallets.from_mnemonics(mnemonics=mnemonics, version=WalletVersionEnum.v3r2, workchain=0)

Метод Wallets.create возвращает 4 метрики:
Мнемонику (mnemonics). Это seed-фраза
Публичный ключ (pub_k);
Приватный ключ (priv_k);
Адрес Кошелька (wallet);
Wallet - это объект класса


	from tonsdk.contract.wallet import Wallets, WalletVersionEnum
	
	    #Кошелек 1
	mnemonics1, pub_key1, priv_k1, wallet1 = Wallets.create(version=WalletVersionEnum.v3r2, workchain=0)
	
	    #Кошелек 2
	mnemonics2, pub_key2, priv_k2, wallet2 = Wallets.create(version=WalletVersionEnum.v3r2, workchain=0)
	
	    #Кошелек 3
	mnemonics3, pub_key3, priv_k3, wallet3 = Wallets.create(version=WalletVersionEnum.v3r2, workchain=0)
	
	    #Кошелек 4 (Казна ДАО)
	mnemonics4, pub_key4, priv_k4, wallet4 = Wallets.create(version=WalletVersionEnum.v3r2, workchain=0)
	
	
	print("___Вывод данных Первого кошелька___")
	print(mnemonics1, pub_key1, priv_k1, wallet1.address.to_string(True, True, True, True), sep='\n', end='\n\n')
	
	print("___Вывод данных Второго кошелька___")
	print(mnemonics2, pub_key2, priv_k2, wallet2.address.to_string(True, True, True, True), sep='\n', end='\n\n')
	
	print("___Вывод данных Третьего кошелька___")
	print(mnemonics3, pub_key3, priv_k3, wallet3.address.to_string(True, True, True, True), sep='\n', end='\n\n')
	
	print("___Вывод данных кошелька Казны ДАО___")
	print(mnemonics4, pub_key4, priv_k4, wallet4.address.to_string(True, True, True, True), sep='\n', end='\n\n')

		['price', 'gas', 'pizza', 'before', 'skirt', 'reform', 'whale', 'around', 'mother', 'flock', 'gown', 'dry', 'target', 'segment', 'stumble', 'help', 'palace', 'bird', 'away', 'jacket', 'dolphin', 'bright', 'change', 'reflect']
		b'\xb2\xd2Y\xaf\xf5h\xd7\x0e\xb1|]i]\xee\xfe\xd8e\x90\xb8\xac<\xfdn\xb2l7s\xbd\x17\xd7\x0e\xb0'
		b'\x9d\xd7\xe2\xb3\xa1\xa7\x1d1\x7fU\xbb\x14\xe5\xcc\xf1\xfeb\xfe\x00\xc25\xb6ME\x17\xa02\xa8\x95\xaa\x84\xf9\xb2\xd2Y\xaf\xf5h\xd7\x0e\xb1|]i]\xee\xfe\xd8e\x90\xb8\xac<\xfdn\xb2l7s\xbd\x17\xd7\x0e\xb0'
		<tonsdk.contract.wallet._wallet_contract_v3.WalletV3ContractR2 object at 0x0000012755E84090>


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
    
 
