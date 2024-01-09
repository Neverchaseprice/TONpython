# TONpython
TON with Python 


# Задача 1: Сделать ТОН-кошелек на TestNet и задеплоить его
Сначала Блок теории, потом блок практики


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
	
	mnemonics1, pub_key1, priv_k1, wallet1 = Wallets.create(version=WalletVersionEnum.v3r2, workchain=0)
	
	print(mnemonics1)
	print(pub_key1)
	print(priv_k1)
	print(wallet1)

		['price', 'gas', 'pizza', 'before', 'skirt', 'reform', 'whale', 'around', 'mother', 'flock', 'gown', 'dry', 'target', 'segment', 'stumble', 'help', 'palace', 'bird', 'away', 'jacket', 'dolphin', 'bright', 'change', 'reflect']
		b'\xb2\xd2Y\xaf\xf5h\xd7\x0e\xb1|]i]\xee\xfe\xd8e\x90\xb8\xac<\xfdn\xb2l7s\xbd\x17\xd7\x0e\xb0'
		b'\x9d\xd7\xe2\xb3\xa1\xa7\x1d1\x7fU\xbb\x14\xe5\xcc\xf1\xfeb\xfe\x00\xc25\xb6ME\x17\xa02\xa8\x95\xaa\x84\xf9\xb2\xd2Y\xaf\xf5h\xd7\x0e\xb1|]i]\xee\xfe\xd8e\x90\xb8\xac<\xfdn\xb2l7s\xbd\x17\xd7\x0e\xb0'
		<tonsdk.contract.wallet._wallet_contract_v3.WalletV3ContractR2 object at 0x0000012755E84090>

Для нашей цели нам надо 3 одинаковых кошелька 

	from tonsdk.contract.wallet import Wallets, WalletVersionEnum
	#from tabulate import tabulate
	
	mnemonics1, pub_key1, priv_k1, wallet1 = Wallets.create(version=WalletVersionEnum.v3r2, workchain=0)
	mnemonics2, pub_key2, priv_k2, wallet2 = Wallets.create(version=WalletVersionEnum.v3r2, workchain=0)
	mnemonics3, pub_key3, priv_k3, wallet3 = Wallets.create(version=WalletVersionEnum.v3r2, workchain=0)
	
	
	#TableWallets = [['mnemonics', 'pub_key', 'priv_k', 'wallet'],[mnemonics1, pub_key1, priv_k1, wallet1],[mnemonics2, pub_key2, priv_k2, wallet2],[mnemonics3, pub_key3, priv_k3, wallet3]]
	#print(tabulate(TableWallets))
	
	
	print("___Вывод данных Первого кошелька___")
	print(mnemonics1)
	print(pub_key1)
	print(priv_k1)
	print(wallet1)
	
	print("___Вывод данных Второго кошелька___")
	print(mnemonics2)
	print(pub_key2)
	print(priv_k2)
	print(wallet2)
	
	print("___Вывод данных Третьего кошелька___")
	print(mnemonics3)
	print(pub_key3)
	print(priv_k3)
	print(wallet3)
 		
		___Вывод данных Первого кошелька___
		['trend', 'winter', 'ceiling', 'metal', 'gate', 'priority', 'allow', 'tower', 'frame', 'decrease', 'teach', 'panda', 'artefact', 'tomato', 'crew', 'select', 'announce', 'body', 'list', 'nephew', 'love', 'dwarf', 'limit', 'soul']
		b'\x89kY\xdf;,8\xef\xe0\x1a:\x82Z\xde\x1c\xff\xe8z\x9f\r\x88,\x83\xd6l\xa0\x83b\xc1\xea3\xd7'
		b'\xfb5\x01I\xb0\x9eme\x17M_\xfb\xf7\xeb\xd5\xce\xff\x99\xda\xcb\xb6BC\xb5\xb5&bRR\xfe\xce\xe1\x89kY\xdf;,8\xef\xe0\x1a:\x82Z\xde\x1c\xff\xe8z\x9f\r\x88,\x83\xd6l\xa0\x83b\xc1\xea3\xd7'
		<tonsdk.contract.wallet._wallet_contract_v3.WalletV3ContractR2 object at 0x000001D4BDB84310>
		___Вывод данных Второго кошелька___
		['lawn', 'put', 'bird', 'fee', 'magnet', 'live', 'device', 'romance', 'wonder', 'above', 'mechanic', 'tonight', 'boy', 'across', 'air', 'fringe', 'winner', 'taste', 'praise', 'situate', 'planet', 'chat', 'romance', 'pistol']
		b'\x85\xa2\xda\xca\x00\xf5K\x92T\xc0u\xc3\xc3\x8cE\xfae\x93p\x97\xfe\xb1\xc7\x93\r\x94\x83\xcb\x8a\xbd\xdei'
		b'\x15\xedoC\xb3\x9bB\xc5\xbd\x0e\x98XJ\xaau\x8d\xb2{:\xc2+,\xf5e\x88T\xbaZ\xa3"\x8c\x17\x85\xa2\xda\xca\x00\xf5K\x92T\xc0u\xc3\xc3\x8cE\xfae\x93p\x97\xfe\xb1\xc7\x93\r\x94\x83\xcb\x8a\xbd\xdei'
		<tonsdk.contract.wallet._wallet_contract_v3.WalletV3ContractR2 object at 0x000001D4BFA005D0>
		___Вывод данных Третьего кошелька___
		['usual', 'gentle', 'verb', 'hidden', 'smooth', 'twist', 'wild', 'ring', 'aspect', 'sample', 'head', 'trade', 'taste', 'left', 'lounge', 'left', 'fan', 'muffin', 'rack', 'disease', 'tired', 'sure', 'improve', 'weather']
		b"4\xbeI\xf0\xfc\xa7\xf9\xf4\xdeH\x12l\xf9\xcf\xe6\x14\xd74R\xef_\xc3\xf4\xba\x89'\x0c\x12+kxh"
		b'\x07R\xd1\xd8z\x1e\xedF\xb6\xfb[\x1aE\x9dQ\xbeWc\xf4BkT^%i\n\xd4\xe5\xe6\x84\xbe"4\xbeI\xf0\xfc\xa7\xf9\xf4\xdeH\x12l\xf9\xcf\xe6\x14\xd74R\xef_\xc3\xf4\xba\x89\'\x0c\x12+kxh'
		<tonsdk.contract.wallet._wallet_contract_v3.WalletV3ContractR2 object at 0x000001D4BFA007D0>









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
    
 
