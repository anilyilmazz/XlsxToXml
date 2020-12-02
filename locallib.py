# -*- coding: utf-8 -*-

def monthToNum(shortMonth):
    return {
            'OCAK DÖNEMİ' : '01',
            'ŞUBAT DÖNEMİ' : '02',
            'MART DÖNEMİ' : '03',
            'NİSAN DÖNEMİ' : '04',
            'MAYIS DÖNEMİ' : '05',
            'HAZİRAN DÖNEMİ' : '06',
            'TEMMUZ DÖNEMİ' : '07',
            'AĞUSTOS DÖNEMİ' : '08',
            'EYLÜL DÖNEMİ' : '09', 
            'EKİM DÖNEMİ' : '10',
            'KASIM DÖNEMİ' : '11',
            'ARALIK DÖNEMİ' : '12'
    }[shortMonth]

def getDateByCode(paymentCode):
    return {
            2 : 7,
            3 : 15,
            4 : 30,
            5 : 45,
            13 : 60,
            14: 90
    }[paymentCode]