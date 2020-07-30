# -*- coding: utf-8 -*-
import pandas as pd
from datetime import date, datetime, timedelta
import requests

xl = pd.ExcelFile("fatura.xlsx")
df = xl.parse("xml")

xml = ''
for i in df.index:
    startDate = datetime.strptime(df['Fatura Tarihi'][i], '%d.%m.%Y').date() - timedelta(30)
    startDate = startDate.strftime("%d-%m-%Y")

    endDate = datetime.strptime(df['Fatura Tarihi'][i], '%d.%m.%Y').date() - timedelta(1)
    endDate = endDate.strftime("%d-%m-%Y")

    dolarUrl = f"https://evds2.tcmb.gov.tr/service/evds/series=TP.DK.USD.A&startDate={startDate}&endDate={endDate}&type=json&key=fTXaeHOQKW"
    dolarList = requests.get(dolarUrl).json()

    for j in reversed((dolarList['items'])):
        if(j['TP_DK_USD_A'] != None):
          dolar = j['TP_DK_USD_A']
          break
             
    xml += f"""  <INVOICE DBOP="INS" >
    <TYPE>9</TYPE>
    <NUMBER></NUMBER>
    <DATE>{df['Fatura Tarihi'][i]}</DATE>
    <TIME>235085636</TIME>
    <AUXIL_CODE>BSTB035114</AUXIL_CODE>
    <AUTH_CODE>{df['Alt Müşteri'][i]}</AUTH_CODE> 
    <ARP_CODE>{df['Logo Cari'][i]}</ARP_CODE>
    <SHIPLOC_CODE>007</SHIPLOC_CODE>
    <GL_CODE>{df['Logo Cari'][i]}</GL_CODE>
    <POST_FLAGS>247</POST_FLAGS>
    <VAT_RATE>{df['KDV Oranı'][i]}</VAT_RATE>
    <TOTAL_DISCOUNTED>{df['Net Fiyat'][i]}</TOTAL_DISCOUNTED>
    <TOTAL_VAT>{df['KDV Fiyat'][i]}</TOTAL_VAT>
    <TOTAL_GROSS>{df['Net Fiyat'][i]}</TOTAL_GROSS>
    <TOTAL_NET>{df['Toplam Fiyat'][i]}</TOTAL_NET>
    <NOTES1>{df['Po No'][i]}</NOTES1>
    <TC_NET>{df['Toplam Fiyat'][i]}</TC_NET>
    <RC_XRATE>{dolar}</RC_XRATE>
    <RC_NET>{"{:.5f}".format(float(df['Toplam Fiyat'][i])/float(dolar))}</RC_NET>
    <PAYMENT_CODE>003</PAYMENT_CODE>
    <CREATED_BY>{df['Ekleyen ID'][i]}</CREATED_BY>
    <DATE_CREATED>{date.today().strftime("%d.%m.%Y")}</DATE_CREATED>
    <HOUR_CREATED>{date.datetime.now().hour}</HOUR_CREATED>
    <MIN_CREATED>{date.datetime.now().minute}</MIN_CREATED>
    <SEC_CREATED>{date.datetime.now().second}</SEC_CREATED>
    <SALESMAN_CODE>{df['Satış Temsilcisi'][i]}</SALESMAN_CODE>
    <CURRSEL_TOTALS>1</CURRSEL_TOTALS>
    <DATA_REFERENCE>0</DATA_REFERENCE>
    <DISPATCHES>
    </DISPATCHES>
    <TRANSACTIONS>
      <TRANSACTION>
        <TYPE>4</TYPE>
        <MASTER_CODE>{df['Ürün Detay'][i]}</MASTER_CODE>
        <GL_CODE1></GL_CODE1>
        <GL_CODE2></GL_CODE2>
        <DELVRY_CODE>{df['Alt Müşteri'][i]}</DELVRY_CODE>
        <QUANTITY>{df['Miktar'][i]}</QUANTITY>
        <PRICE>{df['Birim Fiyat'][i]}</PRICE>
        <TOTAL>{df['Net Fiyat'][i]}</TOTAL>
        <RC_XRATE>{dolar}</RC_XRATE>
        <DESCRIPTION>{df['İş Ortağı Oranı'][i]}</DESCRIPTION>
        <UNIT_CODE>ADET</UNIT_CODE>
        <UNIT_CONV1>1</UNIT_CONV1>
        <UNIT_CONV2>1</UNIT_CONV2>
        <VAT_RATE>{df['KDV Oranı'][i]}</VAT_RATE>
        <VAT_AMOUNT>{df['KDV Fiyat'][i]}</VAT_AMOUNT>
        <VAT_BASE>{df['Net Fiyat'][i]}</VAT_BASE>
        <BILLED>1</BILLED>
        <TOTAL_NET>{df['Net Fiyat'][i]}</TOTAL_NET>
        <DATA_REFERENCE>0</DATA_REFERENCE>
        <DIST_ORD_REFERENCE>0</DIST_ORD_REFERENCE>
        <CAMPAIGN_INFOS>
          <CAMPAIGN_INFO>
          </CAMPAIGN_INFO>
        </CAMPAIGN_INFOS>
        <MULTI_ADD_TAX>0</MULTI_ADD_TAX>
        <EDT_CURR>1</EDT_CURR>
        <EDT_PRICE>{"{:.5f}".format(float(df['Toplam Fiyat'][i])/float(dolar))}</EDT_PRICE>
        <ORGLOGOID></ORGLOGOID>
        <SALEMANCODE>{df['Satış Temsilcisi'][i]}</SALEMANCODE>
        <DEFNFLDSLIST>
        </DEFNFLDSLIST>
        <MONTH>{df['Fatura Tarihi'][i][4:-5]}</MONTH>
        <YEAR>{df['Fatura Tarihi'][i][6:]}</YEAR>
        <PREACCLINES>
        </PREACCLINES>
        <UNIT_GLOBAL_CODE>NIU</UNIT_GLOBAL_CODE>
        <EDTCURR_GLOBAL_CODE>USD</EDTCURR_GLOBAL_CODE>
        <GUID></GUID>
        <AUXIL_CODE2>{df['Kaynak'][i]}</AUXIL_CODE2>
        <MASTER_DEF>ÇAĞRI MERKEZİ BULUT PLATFORMU</MASTER_DEF>
        <FOREIGN_TRADE_TYPE>1</FOREIGN_TRADE_TYPE>
        <DISTRIBUTION_TYPE_WHS>0</DISTRIBUTION_TYPE_WHS>
        <DISTRIBUTION_TYPE_FNO>0</DISTRIBUTION_TYPE_FNO>
        <FUTURE_MONTH_BEGDATE>132384519</FUTURE_MONTH_BEGDATE>
      </TRANSACTION>
    </TRANSACTIONS>
    <PAYMENT_LIST>
      <PAYMENT>
        <DATE></DATE>
        <MODULENR>4</MODULENR>
        <TRCODE>9</TRCODE>
        <TOTAL>{df['Toplam Fiyat'][i]}</TOTAL>
        <DAYS></DAYS>
        <PROCDATE>{df['Fatura Tarihi'][i]}</PROCDATE>
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
        <NUMFLDS1>{df['Fatura Tarihi'][i][4:-5]}</NUMFLDS1>
        <NUMFLDS2>{df['Yinelenen'][i]}</NUMFLDS2>
        <NUMFLDS4>{df['Yeni Hizmet'][i]}</NUMFLDS4>
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
    <DOC_DATE>{df['Fatura Tarihi'][i]}</DOC_DATE>
    <EINVOICE>1</EINVOICE>
    <PROFILE_ID>1</PROFILE_ID>
    <GUID></GUID>
    <EDURATION_TYPE>0</EDURATION_TYPE>
    <EDTCURR_GLOBAL_CODE>USD</EDTCURR_GLOBAL_CODE>
    <TOTAL_NET_STR></TOTAL_NET_STR>
    <SHIPLOC_DEF>{df['Dönem'][i]}</SHIPLOC_DEF>
    <TOTAL_SERVICES>{df['Net Fiyat'][i]}</TOTAL_SERVICES>
    <EXIMVAT>0</EXIMVAT>
    <EARCHIVEDETR_INTPAYMENTTYPE>0</EARCHIVEDETR_INTPAYMENTTYPE>
    <EBOOK_DOCTYPE>99</EBOOK_DOCTYPE>
    <OKCINFO_LIST>
      <OKCINFO>
      </OKCINFO>
    </OKCINFO_LIST>
  </INVOICE>\n"""

xml = f"""<?xml version="1.0" encoding="ISO-8859-9"?>
<SALES_INVOICES>
{xml}</SALES_INVOICES>"""


f = open("fatura.xml", "w", encoding='ISO-8859-9')
f.write(xml)
f.close()