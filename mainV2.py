# -*- coding: utf-8 -*-
import pandas as pd
from datetime import date, datetime, timedelta
import requests

kdv_rate = 18

df = pd.read_excel('fatura.xlsx', sheet_name='xml')
df = df.groupby(by=["Logo Cari", "Alt Müşteri"])

xml = ""
bill = ""
for i in df:
    startDate = datetime.strptime(i[1].iloc[0]['Fatura Tarihi'], '%d.%m.%Y').date() - timedelta(30)
    startDate = startDate.strftime("%d-%m-%Y")

    endDate = datetime.strptime(i[1].iloc[0]['Fatura Tarihi'], '%d.%m.%Y').date() - timedelta(1)
    endDate = endDate.strftime("%d-%m-%Y")

    dolarUrl = f"https://evds2.tcmb.gov.tr/service/evds/series=TP.DK.USD.A&startDate={startDate}&endDate={endDate}&type=json&key=fTXaeHOQKW"
    dolarList = requests.get(dolarUrl).json()

    for m in reversed((dolarList['items'])):
        if(m['TP_DK_USD_A'] != None):
          dolar = float(m['TP_DK_USD_A'])
          break

    k = 0
    transaction = ""
    net_fiyat = 0
    kdv_fiyat = 0
    toplam_fiyat = 0
    dolar_fiyat = 0   
    for j in i[1].index:
        child_net = float(i[1].iloc[k]['Miktar'])*float(i[1].iloc[k]['Birim Fiyat'])
        child_kdv = child_net/100*18
        child_toplam = child_net + child_kdv
        child_dolar = child_toplam / dolar

        transaction += f""" 
        <TRANSACTION>
            <TYPE>4</TYPE>
            <MASTER_CODE>{i[1].iloc[k]['Ürün Detay']}</MASTER_CODE>
            <GL_CODE1></GL_CODE1>
            <GL_CODE2></GL_CODE2>
            <DELVRY_CODE>{i[1].iloc[k]['Alt Müşteri']}</DELVRY_CODE>
            <QUANTITY>{i[1].iloc[k]['Miktar']}</QUANTITY>
            <PRICE>{i[1].iloc[k]['Birim Fiyat']}</PRICE>
            <TOTAL>{child_net}</TOTAL>
            <RC_XRATE>{dolar}</RC_XRATE>
            <DESCRIPTION>{i[1].iloc[k]['İş Ortağı Oranı']}</DESCRIPTION>
            <UNIT_CODE>ADET</UNIT_CODE>
            <UNIT_CONV1>1</UNIT_CONV1>
            <UNIT_CONV2>1</UNIT_CONV2>
            <VAT_RATE>{kdv_rate}</VAT_RATE>
            <VAT_AMOUNT>{child_kdv}</VAT_AMOUNT>
            <VAT_BASE>{child_net}</VAT_BASE>
            <BILLED>1</BILLED>
            <TOTAL_NET>{child_net}</TOTAL_NET>
            <DATA_REFERENCE>0</DATA_REFERENCE>
            <DIST_ORD_REFERENCE>0</DIST_ORD_REFERENCE>
            <CAMPAIGN_INFOS>
            <CAMPAIGN_INFO>
            </CAMPAIGN_INFO>
            </CAMPAIGN_INFOS>
            <MULTI_ADD_TAX>0</MULTI_ADD_TAX>
            <EDT_CURR>1</EDT_CURR>
            <EDT_PRICE>{"{:.5f}".format(child_dolar)}</EDT_PRICE>
            <ORGLOGOID></ORGLOGOID>
            <SALEMANCODE>{i[1].iloc[k]['Satış Temsilcisi']}</SALEMANCODE>
            <DEFNFLDSLIST>
            </DEFNFLDSLIST>
            <MONTH>{i[1].iloc[k]['Fatura Tarihi'][4:-5]}</MONTH>
            <YEAR>{i[1].iloc[k]['Fatura Tarihi'][6:]}</YEAR>
            <PREACCLINES>
            </PREACCLINES>
            <UNIT_GLOBAL_CODE>NIU</UNIT_GLOBAL_CODE>
            <EDTCURR_GLOBAL_CODE>USD</EDTCURR_GLOBAL_CODE>
            <GUID></GUID>
            <AUXIL_CODE2>{i[1].iloc[k]['Kaynak']}</AUXIL_CODE2>
            <MASTER_DEF>ÇAĞRI MERKEZİ BULUT PLATFORMU</MASTER_DEF>
            <FOREIGN_TRADE_TYPE>1</FOREIGN_TRADE_TYPE>
            <DISTRIBUTION_TYPE_WHS>0</DISTRIBUTION_TYPE_WHS>
            <DISTRIBUTION_TYPE_FNO>0</DISTRIBUTION_TYPE_FNO>
            <FUTURE_MONTH_BEGDATE>132384519</FUTURE_MONTH_BEGDATE>
        </TRANSACTION>
        """
        net_fiyat += child_net
        kdv_fiyat += child_kdv
        toplam_fiyat += child_toplam
        dolar_fiyat += child_dolar
        k += 1
             
    bill += f""" 
        <INVOICE DBOP="INS" >
            <TYPE>9</TYPE>
            <NUMBER></NUMBER>
            <DATE>{i[1].iloc[0]['Fatura Tarihi']}</DATE>
            <TIME>235085636</TIME>
            <AUXIL_CODE>BSTB035114</AUXIL_CODE>
            <AUTH_CODE>{i[1].iloc[0]['Alt Müşteri']}</AUTH_CODE> 
            <ARP_CODE>{i[1].iloc[0]['Logo Cari']}</ARP_CODE>
            <SHIPLOC_CODE>007</SHIPLOC_CODE>
            <GL_CODE>{i[1].iloc[0]['Logo Cari']}</GL_CODE>
            <POST_FLAGS>247</POST_FLAGS>
            <VAT_RATE>{kdv_rate}</VAT_RATE>
            <TOTAL_DISCOUNTED>{net_fiyat}</TOTAL_DISCOUNTED>
            <TOTAL_VAT>{kdv_fiyat}</TOTAL_VAT>
            <TOTAL_GROSS>{net_fiyat}</TOTAL_GROSS>
            <TOTAL_NET>{toplam_fiyat}</TOTAL_NET>
            <NOTES1>{i[1].iloc[0]['Po No']}</NOTES1>
            <TC_NET>{toplam_fiyat}</TC_NET>
            <RC_XRATE>{dolar}</RC_XRATE>
            <RC_NET>{"{:.5f}".format(dolar_fiyat)}</RC_NET>
            <PAYMENT_CODE>003</PAYMENT_CODE>
            <CREATED_BY>{i[1].iloc[0]['Ekleyen ID']}</CREATED_BY>
            <DATE_CREATED>{date.today().strftime("%d.%m.%Y")}</DATE_CREATED>
            <HOUR_CREATED>{datetime.now().strftime("%H")}</HOUR_CREATED>
            <MIN_CREATED>{datetime.now().strftime("%M")}</MIN_CREATED>
            <SEC_CREATED>{datetime.now().strftime("%S")}</SEC_CREATED>
            <SALESMAN_CODE>{i[1].iloc[0]['Satış Temsilcisi']}</SALESMAN_CODE>
            <CURRSEL_TOTALS>1</CURRSEL_TOTALS>
            <DATA_REFERENCE>0</DATA_REFERENCE>
            <DISPATCHES>
            </DISPATCHES>
            <TRANSACTIONS>
                {transaction}
            </TRANSACTIONS>
            <PAYMENT_LIST>
                <PAYMENT>
                    <DATE></DATE>
                    <MODULENR>4</MODULENR>
                    <TRCODE>9</TRCODE>
                    <TOTAL>{toplam_fiyat}</TOTAL>
                    <DAYS></DAYS>
                    <PROCDATE>{i[1].iloc[0]['Fatura Tarihi']}</PROCDATE>
                    <REPORTRATE>{dolar}</REPORTRATE>
                    <DATA_REFERENCE>0</DATA_REFERENCE>
                    <DISCOUNT_DUEDATE></DISCOUNT_DUEDATE>
                    <PAY_NO>1</PAY_NO>
                    <DISCTRLIST>
                    </DISCTRLIST>
                    <DISCTRDELLIST>0</DISCTRDELLIST>
                </PAYMENT>
            </PAYMENT_LIST>
            <ORGLOGOID></ORGLOGOID>
            <DEFNFLDSLIST>
            <DEFNFLD>
                <MODULENR>4</MODULENR>
                <PARENTREF></PARENTREF>
                <NUMFLDS1>{i[1].iloc[0]['Fatura Tarihi'][4:-5]}</NUMFLDS1>
                <NUMFLDS2>{i[1].iloc[0]['Yeni Hizmet']}</NUMFLDS2>
                <NUMFLDS4>{i[1].iloc[0]['Yinelenen']}</NUMFLDS4>
                <NUMFLDS5></NUMFLDS5>	
                <XML_ATTRIBUTE>2</XML_ATTRIBUTE>
                <DATA_REFERENCE>0</DATA_REFERENCE>
            </DEFNFLD>
            </DEFNFLDSLIST>
            <DEDUCTIONPART1>2</DEDUCTIONPART1>
            <DEDUCTIONPART2>3</DEDUCTIONPART2>
            <DATA_LINK_REFERENCE>0</DATA_LINK_REFERENCE>
            <INTEL_LIST>
            <INTEL>
            </INTEL>
            </INTEL_LIST>
            <AFFECT_RISK>0</AFFECT_RISK>
            <PREACCLINES>
            </PREACCLINES>
            <DOC_DATE>{i[1].iloc[0]['Fatura Tarihi']}</DOC_DATE>
            <EINVOICE>{i[1].iloc[0]['e fatura/e arşiv']}</EINVOICE>
            <PROFILE_ID>1</PROFILE_ID>
            <GUID></GUID>
            <EDURATION_TYPE>0</EDURATION_TYPE>
            <EDTCURR_GLOBAL_CODE>USD</EDTCURR_GLOBAL_CODE>
            <TOTAL_NET_STR></TOTAL_NET_STR>
            <SHIPLOC_DEF>{i[1].iloc[0]['Dönem']}</SHIPLOC_DEF>
            <TOTAL_SERVICES>{net_fiyat}</TOTAL_SERVICES>
            <EXIMVAT>0</EXIMVAT>
            <EARCHIVEDETR_INTPAYMENTTYPE>0</EARCHIVEDETR_INTPAYMENTTYPE>
            <EBOOK_DOCTYPE>99</EBOOK_DOCTYPE>
            <OKCINFO_LIST>
            <OKCINFO>
            </OKCINFO>
            </OKCINFO_LIST>
        </INVOICE>
        """

xml = f"""<?xml version="1.0" encoding="ISO-8859-9"?>
<SALES_INVOICES>
{bill}
</SALES_INVOICES>"""

f = open("fatura.xml", "w", encoding='ISO-8859-9')
f.write(xml)
f.close()