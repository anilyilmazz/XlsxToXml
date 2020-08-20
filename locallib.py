# -*- coding: utf-8 -*-

def monthToNum(shortMonth):
    return {
            'OCAK DÖNEMİ' : 1,
            'ŞUBAT DÖNEMİ' : 2,
            'MART DÖNEMİ' : 3,
            'NİSAN DÖNEMİ' : 4,
            'MAYIS DÖNEMİ' : 5,
            'HAZİRAN DÖNEMİ' : 6,
            'TEMMUZ DÖNEMİ' : 7,
            'AĞUTOS DÖNEMİ' : 8,
            'EYLÜL DÖNEMİ' : 9, 
            'EKİM DÖNEMİ' : 10,
            'KASIM DÖNEMİ' : 11,
            'ARALIK DÖNEMİ' : 12
    }[shortMonth]