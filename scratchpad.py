#!/usr/bin/env python

import evecentral
import sys

REGION_IDS={
	'Aridia': 10000054,
	'Black Rise': 10000069,
	'Branch': 10000055,
	'Cache': 10000007,
	'Catch': 10000014,
	'Cloud Ring': 10000051,
	'Cobalt Edge': 10000053,
	'Curse': 10000012,
	'Deklein': 10000035,
	'Delve': 10000060,
	'Derelik': 10000001,
	'Detorid': 10000005,
	'Devoid': 10000036,
	'Domain': 10000043,
	'Esoteria': 10000039,
	'Essence': 10000064,
	'Etherium Reach': 10000027,
	'Everyshore': 10000037,
	'Fade': 10000046,
	'Feythabolis': 10000056,
	'Fountain': 10000058,
	'Geminate': 10000029,
	'Genesis': 10000067,
	'Great Wildlands': 10000011,
	'Heimatar': 10000030,
	'Immensea': 10000025,
	'Impass': 10000031,
	'Insmother': 10000009,
	'Kador': 10000052,
	'Khanid': 10000049,
	'Kor-Azor': 10000065,
	'Lonetrek': 10000016,
	'Malpais': 10000013,
	'Metropolis': 10000042,
	'Molden Heath': 10000028,
	'Oasa': 10000040,
	'Omist': 10000062,
	'Outer Passage': 10000021,
	'Outer Ring': 10000057,
	'Paragon Soul': 10000059,
	'Period Basis': 10000063,
	'Perrigen Falls': 10000066,
	'Placid': 10000048,
	'Providence': 10000047,
	'Pure Blind': 10000023,
	'Querious': 10000050,
	'Scalding Pass': 10000008,
	'Sinq Laison': 10000032,
	'Solitude': 10000044,
	'Stain': 10000022,
	'Syndicate': 10000041,
	'Tash-Murkon': 10000020,
	'Tenal': 10000045,
	'Tenerifis': 10000061,
	'The Bleak Lands': 10000038,
	'The Citadel': 10000033,
	'The Forge': 10000002,
	'The Kalevala Expanse': 10000034,
	'The Spire': 10000018,
	'Tribute': 10000010,
	'Vale of the Silent': 10000003,
	'Venal': 10000015,
	'Verge Vendor': 10000068,
	'Wicked Creek': 10000006,
	}

IDS_REGIONS={
	10000054: 'Aridia',
	10000069: 'Black Rise',
	10000055: 'Branch',
	10000007: 'Cache',
	10000014: 'Catch',
	10000051: 'Cloud Ring',
	10000053: 'Cobalt Edge',
	10000012: 'Curse',
	10000035: 'Deklein',
	10000060: 'Delve',
	10000001: 'Derelik',
	10000005: 'Detorid',
	10000036: 'Devoid',
	10000043: 'Domain',
	10000039: 'Esoteria',
	10000064: 'Essence',
	10000027: 'Etherium Reach',
	10000037: 'Everyshore',
	10000046: 'Fade',
	10000056: 'Feythabolis',
	10000058: 'Fountain',
	10000029: 'Geminate',
	10000067: 'Genesis',
	10000011: 'Great Wildlands',
	10000030: 'Heimatar',
	10000025: 'Immensea',
	10000031: 'Impass',
	10000009: 'Insmother',
	10000052: 'Kador',
	10000049: 'Khanid',
	10000065: 'Kor-Azor',
	10000016: 'Lonetrek',
	10000013: 'Malpais',
	10000042: 'Metropolis',
	10000028: 'Molden Heath',
	10000040: 'Oasa',
	10000062: 'Omist',
	10000021: 'Outer Passage',
	10000057: 'Outer Ring',
	10000059: 'Paragon Soul',
	10000063: 'Period Basis',
	10000066: 'Perrigen Falls',
	10000048: 'Placid',
	10000047: 'Providence',
	10000023: 'Pure Blind',
	10000050: 'Querious',
	10000008: 'Scalding Pass',
	10000032: 'Sinq Laison',
	10000044: 'Solitude',
	10000022: 'Stain',
	10000041: 'Syndicate',
	10000020: 'Tash-Murkon',
	10000045: 'Tenal',
	10000061: 'Tenerifis',
	10000038: 'The Bleak Lands',
	10000033: 'The Citadel',
	10000002: 'The Forge',
	10000034: 'The Kalevala Expanse',
	10000018: 'The Spire',
	10000010: 'Tribute',
	10000003: 'Vale of the Silent',
	10000015: 'Venal',
	10000068: 'Verge Vendor',
	10000006: 'Wicked Creek',
	}

HISEC_REGION_IDS=[
	10000033, # The Citadel
	10000001, # Derelik
	10000036, # Devoid
	10000043, # Domain
	10000064, # Essence
	10000037, # Everyshore
	10000002, # The Forge
	10000067, # Genesis
	10000030, # Heimatar
	10000052, # Kador
	10000049, # Khanid
	10000065, # Kor-Azor
	10000016, # Lonetrek
	10000042, # Metropolis
	10000028, # Molden Heath (Home!)
	10000032, # Sinq Laison
	10000020, # Tash-Murkon
	10000068, # Verge Vendor
	]

__all__ = ("HISEC_REGION_IDS", "REGION_IDS", "best_price")

def collect_stats(item_name, regions=HISEC_REGION_IDS):
	stats = {}
	for region in HISEC_REGION_IDS:
		stats[region] = evecentral.market_stats(item_name, region)
	return stats

def check_bids(item_name, regions=HISEC_REGION_IDS):
	maxbuy = None
	minbuy = None
	minsell = None
	maxsell = None
	nobuy = []
	nosell = []
	stats = collect_stats(item_name, regions)
	for region in HISEC_REGION_IDS:
		region_minsell = stats[region]['minsell']
		region_maxbuy = stats[region]['maxbuy']
		# Highest buy order for this item, anywhere
		if (maxbuy is None) or (region_maxbuy > maxbuy['value']):
			maxbuy = {'region': region, 'value': region_maxbuy}
		# Lowest buy order for this item, anywhere
		if ((minsell is None) or (region_minsell < minsell['value'])) and (region_minsell > 0):
			minsell = {'region':region, 'value': region_minsell}
		# Lowest buy order (i.e.: we can overbid)
		if ((minbuy is None) or (region_maxbuy < minbuy['value'])) and (region_maxbuy > 0):
			minbuy = {'region': region, 'value': region_maxbuy}
		# Highest sell order (i.e.: we can underbid)
		if (maxsell is None) or (region_minsell > maxsell['value']):
			maxsell = {'region':region, 'value': region_minsell}
		if (region_minsell == 0):
			nosell.append(region)
		if (region_maxbuy == 0):
			nobuy.append(region)
	return {
		'stats': stats,
		'minsell': minsell,
		'maxsell': maxsell,
		'maxbuy': maxbuy,
		'minbuy': minbuy,
		'nobuy': nobuy,
		'nosell': nosell,
		}

if __name__ == '__main__':
	item_name = sys.argv[1]
	print "Item name: {0}.\n".format(item_name)
	bids = check_bids(item_name)
	print "  Highest buy order: {0} with {1}".format(IDS_REGIONS[bids['maxbuy']['region']], bids['maxbuy']['value'])
	print "  Lowest buy order: {0} with {1}".format(IDS_REGIONS[bids['minbuy']['region']], bids['minbuy']['value'])
	print "  Lowest sell order: {0} with {1}".format(IDS_REGIONS[bids['minsell']['region']], bids['minsell']['value'])
	print "  Highest sell order: {0} with {1}".format(IDS_REGIONS[bids['maxsell']['region']], bids['maxsell']['value'])
