import csv
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from datetime import datetime
from datetime import timezone
from web3 import Web3
import json
import requests
web3 = Web3(Web3.HTTPProvider('http://192.168.0.24:8545'))

start_block_num = 8125000
end_block_num = 8169663
ETH_SCALE = 1000000000000000000
DUST_LIMIT = 10.5

INNER_LIQUID_LINE = 2000
OUTER_LIQUID_LINE = 20000
OASIS0X = '0x39755357759cE0d7f32dC8dC45414CCa409AE24e'
WETH0X = '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2'
DAI0X = '0x89d24A6b4CcB1B6fAA2625fE562bDD9a23260359'
OASIS_ABI = '[{"constant":true,"inputs":[],"name":"matchingEnabled","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"sell_gem","type":"address"},{"name":"buy_gem","type":"address"}],"name":"getBestOffer","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"pay_gem","type":"address"},{"name":"pay_amt","type":"uint256"},{"name":"buy_gem","type":"address"},{"name":"min_fill_amount","type":"uint256"}],"name":"sellAllAmount","outputs":[{"name":"fill_amt","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[],"name":"stop","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"pay_gem","type":"address"},{"name":"buy_gem","type":"address"},{"name":"pay_amt","type":"uint128"},{"name":"buy_amt","type":"uint128"}],"name":"make","outputs":[{"name":"","type":"bytes32"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"owner_","type":"address"}],"name":"setOwner","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"buy_gem","type":"address"},{"name":"pay_gem","type":"address"},{"name":"pay_amt","type":"uint256"}],"name":"getBuyAmount","outputs":[{"name":"fill_amt","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"pay_amt","type":"uint256"},{"name":"pay_gem","type":"address"},{"name":"buy_amt","type":"uint256"},{"name":"buy_gem","type":"address"},{"name":"pos","type":"uint256"}],"name":"offer","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"id","type":"uint256"},{"name":"pos","type":"uint256"}],"name":"insert","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"last_offer_id","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"matchingEnabled_","type":"bool"}],"name":"setMatchingEnabled","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"id","type":"uint256"}],"name":"cancel","outputs":[{"name":"success","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"id","type":"uint256"}],"name":"getOffer","outputs":[{"name":"","type":"uint256"},{"name":"","type":"address"},{"name":"","type":"uint256"},{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"id","type":"uint256"}],"name":"del_rank","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"id","type":"bytes32"},{"name":"maxTakeAmount","type":"uint128"}],"name":"take","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"pay_gem","type":"address"}],"name":"getMinSell","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"getTime","outputs":[{"name":"","type":"uint64"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"dustId","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"id","type":"uint256"}],"name":"getNextUnsortedOffer","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"close_time","outputs":[{"name":"","type":"uint64"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"},{"name":"","type":"address"}],"name":"_span","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"},{"name":"","type":"address"}],"name":"_best","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"stopped","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"id_","type":"bytes32"}],"name":"bump","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"authority_","type":"address"}],"name":"setAuthority","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"sell_gem","type":"address"},{"name":"buy_gem","type":"address"}],"name":"getOfferCount","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"buy_gem","type":"address"},{"name":"buy_amt","type":"uint256"},{"name":"pay_gem","type":"address"},{"name":"max_fill_amount","type":"uint256"}],"name":"buyAllAmount","outputs":[{"name":"fill_amt","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"id","type":"uint256"}],"name":"isActive","outputs":[{"name":"active","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"","type":"uint256"}],"name":"offers","outputs":[{"name":"pay_amt","type":"uint256"},{"name":"pay_gem","type":"address"},{"name":"buy_amt","type":"uint256"},{"name":"buy_gem","type":"address"},{"name":"owner","type":"address"},{"name":"timestamp","type":"uint64"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"getFirstUnsortedOffer","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"owner","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"id","type":"uint256"}],"name":"getBetterOffer","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"_dust","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"id","type":"uint256"}],"name":"getWorseOffer","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"","type":"uint256"}],"name":"_near","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"id","type":"bytes32"}],"name":"kill","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"pay_gem","type":"address"},{"name":"dust","type":"uint256"}],"name":"setMinSell","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"authority","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"isClosed","outputs":[{"name":"closed","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"","type":"uint256"}],"name":"_rank","outputs":[{"name":"next","type":"uint256"},{"name":"prev","type":"uint256"},{"name":"delb","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"id","type":"uint256"}],"name":"getOwner","outputs":[{"name":"owner","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"id","type":"uint256"}],"name":"isOfferSorted","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"buyEnabled_","type":"bool"}],"name":"setBuyEnabled","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"id","type":"uint256"},{"name":"amount","type":"uint256"}],"name":"buy","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"pay_amt","type":"uint256"},{"name":"pay_gem","type":"address"},{"name":"buy_amt","type":"uint256"},{"name":"buy_gem","type":"address"},{"name":"pos","type":"uint256"},{"name":"rounding","type":"bool"}],"name":"offer","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"pay_amt","type":"uint256"},{"name":"pay_gem","type":"address"},{"name":"buy_amt","type":"uint256"},{"name":"buy_gem","type":"address"}],"name":"offer","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"buyEnabled","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"pay_gem","type":"address"},{"name":"buy_gem","type":"address"},{"name":"buy_amt","type":"uint256"}],"name":"getPayAmount","outputs":[{"name":"fill_amt","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"inputs":[{"name":"close_time","type":"uint64"}],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":true,"inputs":[{"indexed":true,"name":"sig","type":"bytes4"},{"indexed":true,"name":"guy","type":"address"},{"indexed":true,"name":"foo","type":"bytes32"},{"indexed":true,"name":"bar","type":"bytes32"},{"indexed":false,"name":"wad","type":"uint256"},{"indexed":false,"name":"fax","type":"bytes"}],"name":"LogNote","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"id","type":"uint256"}],"name":"LogItemUpdate","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"pay_amt","type":"uint256"},{"indexed":true,"name":"pay_gem","type":"address"},{"indexed":false,"name":"buy_amt","type":"uint256"},{"indexed":true,"name":"buy_gem","type":"address"}],"name":"LogTrade","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"id","type":"bytes32"},{"indexed":true,"name":"pair","type":"bytes32"},{"indexed":true,"name":"maker","type":"address"},{"indexed":false,"name":"pay_gem","type":"address"},{"indexed":false,"name":"buy_gem","type":"address"},{"indexed":false,"name":"pay_amt","type":"uint128"},{"indexed":false,"name":"buy_amt","type":"uint128"},{"indexed":false,"name":"timestamp","type":"uint64"}],"name":"LogMake","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"id","type":"bytes32"},{"indexed":true,"name":"pair","type":"bytes32"},{"indexed":true,"name":"maker","type":"address"},{"indexed":false,"name":"pay_gem","type":"address"},{"indexed":false,"name":"buy_gem","type":"address"},{"indexed":false,"name":"pay_amt","type":"uint128"},{"indexed":false,"name":"buy_amt","type":"uint128"},{"indexed":false,"name":"timestamp","type":"uint64"}],"name":"LogBump","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"id","type":"bytes32"},{"indexed":true,"name":"pair","type":"bytes32"},{"indexed":true,"name":"maker","type":"address"},{"indexed":false,"name":"pay_gem","type":"address"},{"indexed":false,"name":"buy_gem","type":"address"},{"indexed":true,"name":"taker","type":"address"},{"indexed":false,"name":"take_amt","type":"uint128"},{"indexed":false,"name":"give_amt","type":"uint128"},{"indexed":false,"name":"timestamp","type":"uint64"}],"name":"LogTake","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"id","type":"bytes32"},{"indexed":true,"name":"pair","type":"bytes32"},{"indexed":true,"name":"maker","type":"address"},{"indexed":false,"name":"pay_gem","type":"address"},{"indexed":false,"name":"buy_gem","type":"address"},{"indexed":false,"name":"pay_amt","type":"uint128"},{"indexed":false,"name":"buy_amt","type":"uint128"},{"indexed":false,"name":"timestamp","type":"uint64"}],"name":"LogKill","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"authority","type":"address"}],"name":"LogSetAuthority","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"owner","type":"address"}],"name":"LogSetOwner","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"isEnabled","type":"bool"}],"name":"LogBuyEnabled","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"pay_gem","type":"address"},{"indexed":false,"name":"min_amount","type":"uint256"}],"name":"LogMinSell","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"isEnabled","type":"bool"}],"name":"LogMatchingEnabled","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"id","type":"uint256"}],"name":"LogUnsortedOffer","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"id","type":"uint256"}],"name":"LogSortedOffer","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"keeper","type":"address"},{"indexed":false,"name":"id","type":"uint256"}],"name":"LogInsert","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"keeper","type":"address"},{"indexed":false,"name":"id","type":"uint256"}],"name":"LogDelete","type":"event"}]'
WETH_ABI = json.loads('[{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"guy","type":"address"},{"name":"wad","type":"uint256"}],"name":"approve","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"src","type":"address"},{"name":"dst","type":"address"},{"name":"wad","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"wad","type":"uint256"}],"name":"withdraw","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"balanceOf","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"dst","type":"address"},{"name":"wad","type":"uint256"}],"name":"transfer","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[],"name":"deposit","outputs":[],"payable":true,"stateMutability":"payable","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"},{"name":"","type":"address"}],"name":"allowance","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"payable":true,"stateMutability":"payable","type":"fallback"},{"anonymous":false,"inputs":[{"indexed":true,"name":"src","type":"address"},{"indexed":true,"name":"guy","type":"address"},{"indexed":false,"name":"wad","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"src","type":"address"},{"indexed":true,"name":"dst","type":"address"},{"indexed":false,"name":"wad","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"dst","type":"address"},{"indexed":false,"name":"wad","type":"uint256"}],"name":"Deposit","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"src","type":"address"},{"indexed":false,"name":"wad","type":"uint256"}],"name":"Withdrawal","type":"event"}]')
DAI_ABI = json.loads('[{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"stop","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"guy","type":"address"},{"name":"wad","type":"uint256"}],"name":"approve","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"owner_","type":"address"}],"name":"setOwner","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"src","type":"address"},{"name":"dst","type":"address"},{"name":"wad","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"guy","type":"address"},{"name":"wad","type":"uint256"}],"name":"mint","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"wad","type":"uint256"}],"name":"burn","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"name_","type":"bytes32"}],"name":"setName","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"src","type":"address"}],"name":"balanceOf","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"stopped","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"authority_","type":"address"}],"name":"setAuthority","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"owner","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"guy","type":"address"},{"name":"wad","type":"uint256"}],"name":"burn","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"wad","type":"uint256"}],"name":"mint","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"dst","type":"address"},{"name":"wad","type":"uint256"}],"name":"transfer","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"dst","type":"address"},{"name":"wad","type":"uint256"}],"name":"push","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"src","type":"address"},{"name":"dst","type":"address"},{"name":"wad","type":"uint256"}],"name":"move","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[],"name":"start","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"authority","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"guy","type":"address"}],"name":"approve","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"src","type":"address"},{"name":"guy","type":"address"}],"name":"allowance","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"src","type":"address"},{"name":"wad","type":"uint256"}],"name":"pull","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"inputs":[{"name":"symbol_","type":"bytes32"}],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"name":"guy","type":"address"},{"indexed":false,"name":"wad","type":"uint256"}],"name":"Mint","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"guy","type":"address"},{"indexed":false,"name":"wad","type":"uint256"}],"name":"Burn","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"authority","type":"address"}],"name":"LogSetAuthority","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"owner","type":"address"}],"name":"LogSetOwner","type":"event"},{"anonymous":true,"inputs":[{"indexed":true,"name":"sig","type":"bytes4"},{"indexed":true,"name":"guy","type":"address"},{"indexed":true,"name":"foo","type":"bytes32"},{"indexed":true,"name":"bar","type":"bytes32"},{"indexed":false,"name":"wad","type":"uint256"},{"indexed":false,"name":"fax","type":"bytes"}],"name":"LogNote","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"src","type":"address"},{"indexed":true,"name":"guy","type":"address"},{"indexed":false,"name":"wad","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"src","type":"address"},{"indexed":true,"name":"dst","type":"address"},{"indexed":false,"name":"wad","type":"uint256"}],"name":"Transfer","type":"event"}]')

oasis_contract = web3.eth.contract(address=OASIS0X, abi=OASIS_ABI)
weth_contract = web3.eth.contract(address=WETH0X, abi=WETH_ABI)
dai_contract = web3.eth.contract(address=DAI0X, abi=DAI_ABI)


class oasis_block:
	timestamp = 0
	block_num = 0
	book = []

class offer:
	price = 0
	boa = 0
	dai_remaining = 0
	oid = 0
	#maker = ''
	def setOffer(self, p, boa, d, oid):
		self.price = p
		self.boa = boa
		self.dai_remaining = d
		self.oid = oid
		

def main():
	# going to put a bunch of oasis_block objects in here
	oblocks = []
	ob = oasis_block()
	# loop through all the blocks
	start_block = web3.eth.getBlock(start_block_num)
	start_dt = datetime.fromtimestamp(start_block['timestamp'])
	ts = datetime(year=start_dt.year, month=start_dt.month, day=start_dt.day, hour=start_dt.hour, minute=start_dt.minute, second=start_dt.second)
	ts.replace(tzinfo=timezone.utc)
	start_day = ts.day
	for i in range(start_block_num, end_block_num):
		# # get the block
		block = web3.eth.getBlock(i)
		timestamp = block['timestamp']
		
		# these will contain offer objects
		# at the end of each block I tally up the differences compared to the current book
		# then go to the next block in the loop
		logmakes = []
		logkills = []
		logtakes = []
		logmakes_pre = []
		logkills_pre = []
		logtakes_pre = []
		# this gets all of the events I care about block they happened
		make_filter = oasis_contract.events.LogMake.createFilter(fromBlock=i, toBlock=i)
		kill_filter = oasis_contract.events.LogKill.createFilter(fromBlock=i, toBlock=i)
		take_filter = oasis_contract.events.LogTake.createFilter(fromBlock=i, toBlock=i)
		logmakes_pre = make_filter.get_all_entries()
		logkills_pre = kill_filter.get_all_entries()
		logtakes_pre = take_filter.get_all_entries()



		if ((len(logmakes_pre) != 0) or (len(logkills_pre) != 0) or (len(logtakes_pre) != 0)):
			if (len(oblocks) != 0):
				ob.book = oblocks[len(oblocks) - 1].book
			else:
				ob.book = []
			ob.block_num = i
			ob.timestamp = timestamp	

		
			# add the logmakes 
			for j in range(0, len(logmakes_pre)):
				# get the offerID
				makestr = str(web3.toHex(logmakes_pre[j]['args']['id']))
				makestr = makestr[2:66].lstrip('0')
				idd = int(makestr, 16)
				# get the paygem and buygem
				paygem = logmakes_pre[j]['args']['pay_gem']
				buygem = logmakes_pre[j]['args']['buy_gem']
				boa = 0
				payamt = logmakes_pre[j]['args']['pay_amt'] / ETH_SCALE
				buyamt = logmakes_pre[j]['args']['buy_amt'] / ETH_SCALE
				str_maker = str(logmakes_pre[j]['args']['maker'])

				# making sure it is for DAI or WETH and not MKR or doughnuts 
				if((paygem == DAI0X) and (buygem == WETH0X)):
					boa = 1
					price = payamt / buyamt
					amtdai = payamt
				if((paygem == WETH0X) and (buygem == DAI0X)):
					boa = -1
					price = buyamt / payamt
					amtdai = buyamt
				if(boa != 0):
					new_offer = offer()
					new_offer.setOffer(price, boa, amtdai, idd)
					logmakes.append(new_offer)

			# add the logkills 
			for j in range(0, len(logkills_pre)):
				makestr = str(web3.toHex(logkills_pre[j]['args']['id']))
				makestr = makestr[2:66].lstrip('0')
				idd = int(makestr, 16)
				logkills.append(idd)

			# add the logtakes 
			for j in range(0, len(logtakes_pre)):
				makestr = str(web3.toHex(logtakes_pre[j]['args']['id']))
				makestr = makestr[2:66].lstrip('0')
				idd = int(makestr, 16)
				paygem = logtakes_pre[j]['args']['pay_gem']
				buygem = logtakes_pre[j]['args']['buy_gem']
				boa = 0
				payamt = logtakes_pre[j]['args']['give_amt'] / ETH_SCALE
				buyamt = logtakes_pre[j]['args']['take_amt'] / ETH_SCALE
				

				# making sure it is for DAI or WETH and not MKR or doughnuts 
				if((paygem == WETH0X) and (buygem == DAI0X)):
					boa = 1
					amtdai = payamt

				if((paygem == DAI0X) and (buygem == WETH0X)):
					boa = -1
					amtdai = buyamt

				if(boa != 0):
					taken_offer = offer()
					taken_offer.setOffer(-1, boa, amtdai, idd)
					logtakes.append(taken_offer)


			# add new limit orders
			ob = add_makes(logmakes, ob)
			# remove killed
			ob = remove_kills(logkills, ob)
			# subtract dai amts from old orders
			ob = sub_takes(logtakes, ob)
			# remove the small ones
			ob = remove_dust(ob)
			# make copy of book
			obb = oasis_block()
			obb.block_num = ob.block_num
			obb.timestamp = ob.timestamp
			obb.book = list.copy(ob.book)
			# add to oblock list
			oblocks.append(obb)

		current_datetime = datetime.fromtimestamp(timestamp)
		ts = datetime(year=current_datetime.year, month=current_datetime.month, day=current_datetime.day, hour=current_datetime.hour, minute=current_datetime.minute, second=current_datetime.second)
		ts.replace(tzinfo=timezone.utc)
		current_day = ts.day
		print('endblock: {0}, timestamp: {1}, datetime: {2}'.format(i, timestamp, ts))

		# output to csv once per day at 0:00 utc
		if(current_day != start_day):
			end_block = block
			outf = start_dt.strftime("{0}-{1}_%Y%m%d".format(start_block['number'], end_block['number'] - 1))
			print("saving: {0}".format(outf))
			output_day(oblocks, start_block['number'], end_block['number'] - 1, outf)
			start_block = block
			start_day = current_datetime.day
			start_dt = ts


def add_makes(logmakes, ob):
	for w in logmakes:
		ob.book.append(w)
	return ob

def remove_kills(logkills, ob):
	indx = []
	# probably a better way to do this
	for w in logkills:
		for p in range(0, len(ob.book)):
			if(ob.book[p].oid == w):
				indx.append(p)

	rem_count = 0
	if(len(indx) != 0):
		indx.sort()
		for w in indx:
			ss = ob.book.pop(w - rem_count)
			rem_count += 1
		
	return ob

def sub_takes(logtakes, ob):
	for w in logtakes:
		for p in range(0, len(ob.book)):
			if(w.oid == ob.book[p].oid):
				ob.book[p].dai_remaining -= w.dai_remaining
	return ob

def remove_dust(ob):
	indx = []
	for w in range(0, len(ob.book)):
		if (abs(ob.book[w].dai_remaining) < DUST_LIMIT):
			indx.append(w)

	rem_count = 0
	if(len(indx) != 0):
		indx.sort()
		for w in indx:
			ss = ob.book.pop(w - rem_count)
			rem_count += 1
		
	return ob

def print_book(oblocks):
	if (len(oblocks) != 0):
		book = oblocks[len(oblocks) - 1].book
		time = oblocks[len(oblocks) - 1].timestamp
		num = oblocks[len(oblocks) - 1].block_num
		print('block_num: {0}, timestamp: {1}'.format(num, time))
		for w in book:
			print('price: {0}, boa: {1}, dai_remaining: {2}, oid: {3}'.format(w.price, w.boa, w.dai_remaining, w.oid))



def output_day(oblocks, start_b, end_b, filenam):
	xl = []
	yl = []
	sl = []
	cl = []
	bl = []
	tl = []
	mk = []


	delt_b = end_b - start_b
	print (delt_b)
	print(len(oblocks))
	#find the index of first block
	indx = 0
	for i in range(0, len(oblocks)):
		if(oblocks[i].block_num >= start_b):
			indx = i
			break

	eth_blocks = start_b
	for i in range(indx, len(oblocks)):
		if(oblocks[i].block_num != eth_blocks):
			dif = oblocks[i].block_num - eth_blocks
			for k in range(0,dif):
				for w in range(0, len(oblocks[i-1].book)):
					if(oblocks[i-1].book[w].boa == 1):
						xl.append(eth_blocks)
						yl.append(oblocks[i-1].book[w].price)
						sl.append(oblocks[i-1].book[w].dai_remaining)
						bl.append(oblocks[i-1].book[w].boa)
						tl.append(oblocks[i-1].timestamp)
						#mk.append(oblocks[i-1].book[w].maker)
					elif(oblocks[i-1].book[w].boa == -1):
						xl.append(eth_blocks)
						yl.append(oblocks[i-1].book[w].price)
						sl.append(oblocks[i-1].book[w].dai_remaining)
						bl.append(oblocks[i-1].book[w].boa)
						tl.append(oblocks[i-1].timestamp)
						#mk.append(oblocks[i-1].book[w].maker)

				eth_blocks += 1

		for j in range(0, len(oblocks[i].book)):
			if(oblocks[i].book[j].boa == 1):
				xl.append(oblocks[i].block_num)
				yl.append(oblocks[i].book[j].price)
				sl.append(oblocks[i].book[j].dai_remaining)
				bl.append(oblocks[i].book[j].boa)
				tl.append(oblocks[i].timestamp)
				#mk.append(oblocks[i].book[j].maker)
			elif(oblocks[i].book[j].boa == -1):
				xl.append(oblocks[i].block_num)
				yl.append(oblocks[i].book[j].price)
				sl.append(oblocks[i].book[j].dai_remaining)
				bl.append(oblocks[i].book[j].boa)
				tl.append(oblocks[i].timestamp)
				#mk.append(oblocks[i].book[j].maker)

		eth_blocks += 1
	ind = np.argwhere(np.absolute(sl) < DUST_LIMIT)
	x2 = np.delete(xl, ind)
	y2 = np.delete(yl, ind)
	s2 = np.delete(sl, ind)
	boa2 = np.delete(bl, ind)
	ts2 = np.delete(tl, ind)

	x = np.around(x2, decimals=0)
	y = np.around(y2, decimals=4)
	s = np.around(s2, decimals=4)
	#c = np.array(cl).astype(np.float64)
	boa = np.around(boa2, decimals=0)
	ts = np.around(ts2, decimals=0)
	#mak = np.array(mk).astype(np.unicode_)
	# this gave a memory error so I quit
	# a = np.asarray([x, y, s, boa, ts, mak])
	# b = a.T
	a = np.asarray([x, y, s, boa, ts])
	b = a.T
	#np.savetxt(filenam + ".csv", b, header="blocknumber,price,remaining_dai,bidorask,timestamp,maker", fmt='%s', delimiter=",", newline="\n")
	np.savetxt(filenam + ".csv", b, header="blocknumber,price,remaining_dai,bidorask,timestamp", fmt='%i,%1.4f,%1.4f,%i,%i', delimiter=",", newline="\n")


if __name__ == "__main__":
	main()

