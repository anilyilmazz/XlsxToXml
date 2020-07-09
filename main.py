import pandas as pd

xl = pd.ExcelFile("fatura.xlsx")
df = xl.parse("xml")

xml = ''
for i in df.index:
    xml += f"""<INVOICE DBOP="INS">
        <TYPE>9</TYPE>
        <NUMBER></NUMBER>
        <DATE>09.07.2020</DATE>
        <TIME>235085636</TIME>
        <AUXIL_CODE>BSTB035114</AUXIL_CODE>
        <AUTH_CODE>{df['Alt Müşteri'][i]}</AUTH_CODE> 
        <ARP_CODE>{df['LOGO CARİ'][i]}</ARP_CODE>
        <SHIPLOC_CODE>007</SHIPLOC_CODE>
        <GL_CODE>{df['LOGO CARİ'][i]}</GL_CODE>
        <POST_FLAGS>247</POST_FLAGS>
        <VAT_RATE>18</VAT_RATE>
        <TOTAL_DISCOUNTED>200</TOTAL_DISCOUNTED>
        <TOTAL_VAT>36</TOTAL_VAT>
        <TOTAL_GROSS>200</TOTAL_GROSS>
        <TOTAL_NET>236</TOTAL_NET>
        <NOTES1>PO:123456</NOTES1>
        <TC_NET>236</TC_NET>
        <RC_XRATE>6.8422</RC_XRATE>
        <RC_NET>34.49</RC_NET>
        <PAYMENT_CODE>003</PAYMENT_CODE>
        <CREATED_BY>5</CREATED_BY>
        <DATE_CREATED>08.07.2020</DATE_CREATED>
        <HOUR_CREATED>14</HOUR_CREATED>
        <MIN_CREATED>15</MIN_CREATED>
        <SEC_CREATED>9</SEC_CREATED>
        <MODIFIED_BY>5</MODIFIED_BY>
        <DATE_MODIFIED>08.07.2020</DATE_MODIFIED>
        <HOUR_MODIFIED>15</HOUR_MODIFIED>
        <MIN_MODIFIED>4</MIN_MODIFIED>
        <SEC_MODIFIED>2</SEC_MODIFIED>
        <SALESMAN_CODE>{df['Satışçı'][i]}</SALESMAN_CODE>
        <CURRSEL_TOTALS>1</CURRSEL_TOTALS>
        <DATA_REFERENCE>2940</DATA_REFERENCE>
        <DISPATCHES>
        </DISPATCHES>
        <TRANSACTIONS>
            <TRANSACTION>
                <TYPE>4</TYPE>
                <MASTER_CODE>{df['Ürün Detay'][i]}</MASTER_CODE>
                <GL_CODE1>600.01.001.0001</GL_CODE1>
                <GL_CODE2>391.01.001.0001</GL_CODE2>
                <DELVRY_CODE>{df['Alt Müşteri'][i]}</DELVRY_CODE>
                <QUANTITY>1</QUANTITY>
                <PRICE>200</PRICE>
                <TOTAL>200</TOTAL>
                <RC_XRATE>6.8422</RC_XRATE>
                <DESCRIPTION>20</DESCRIPTION>
                <UNIT_CODE>ADET</UNIT_CODE>
                <UNIT_CONV1>1</UNIT_CONV1>
                <UNIT_CONV2>1</UNIT_CONV2>
                <VAT_RATE>18</VAT_RATE>
                <VAT_AMOUNT>36</VAT_AMOUNT>
                <VAT_BASE>200</VAT_BASE>
                <BILLED>1</BILLED>
                <TOTAL_NET>200</TOTAL_NET>
                <DATA_REFERENCE>4349</DATA_REFERENCE>
                <DIST_ORD_REFERENCE>0</DIST_ORD_REFERENCE>
                <CAMPAIGN_INFOS>
                <CAMPAIGN_INFO>
                    </CAMPAIGN_INFO>
                    </CAMPAIGN_INFOS>
                <MULTI_ADD_TAX>0</MULTI_ADD_TAX>
                <EDT_CURR>1</EDT_CURR>
                <EDT_PRICE>29.23036</EDT_PRICE>
                <ORGLOGOID></ORGLOGOID>
                <SALEMANCODE>{df['Satışçı'][i]}</SALEMANCODE>
                <DEFNFLDSLIST>
                </DEFNFLDSLIST>
                <MONTH>7</MONTH>
                <YEAR>2020</YEAR>
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
                <DATE>22.07.2020</DATE>
                <MODULENR>4</MODULENR>
                <TRCODE>9</TRCODE>
                <TOTAL>236</TOTAL>
                <DAYS>15</DAYS>
                <PROCDATE>08.07.2020</PROCDATE>
                <REPORTRATE>6.8422</REPORTRATE>
                <DATA_REFERENCE>0</DATA_REFERENCE>
                <DISCOUNT_DUEDATE>22.07.2020</DISCOUNT_DUEDATE>
                <PAY_NO>1</PAY_NO>
                <DISCTRLIST>
                </DISCTRLIST>
                <DISCTRDELLIST>0</DISCTRDELLIST>
            </PAYMENT>
        <PAYMENT_LIST>
        <ORGLOGOID></ORGLOGOID>
        <DEFNFLDSLIST>
            <DEFNFLD>
                <MODULENR>4</MODULENR>
                <PARENTREF>2940</PARENTREF>
                <NUMFLDS1>7</NUMFLDS1>
                <NUMFLDS2>2</NUMFLDS2>
                <NUMFLDS4>1</NUMFLDS4>
                <XML_ATTRIBUTE>2</XML_ATTRIBUTE>
                <DATA_REFERENCE>0</DATA_REFERENCE>
            </DEFNFLD>
        </DEFNFLDSLIST>
        <DEDUCTIONPART1>2</DEDUCTIONPART1>
        <DEDUCTIONPART2>3</DEDUCTIONPART2>
        <DATA_LINK_REFERENCE>2940</DATA_LINK_REFERENCE>
        <INTEL_LIST>
            <INTEL>
            </INTEL>
        </INTEL_LIST>
        <AFFECT_RISK>0</AFFECT_RISK>
        <PREACCLINES>
        </PREACCLINES>
        <DOC_DATE>08.07.2020</DOC_DATE>
        <EINVOICE>1</EINVOICE>
        <PROFILE_ID>1</PROFILE_ID>
        <GUID></GUID>
        <EDURATION_TYPE>0</EDURATION_TYPE>
        <EDTCURR_GLOBAL_CODE>USD</EDTCURR_GLOBAL_CODE>
        <TOTAL_NET_STR>İkiYüzOtuzAltı TL</TOTAL_NET_STR>
        <SHIPLOC_DEF>TEMMUZ DÖNEMİ</SHIPLOC_DEF>
        <TOTAL_SERVICES>200</TOTAL_SERVICES>
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
{xml}
</SALES_INVOICES>"""


f = open("fatura.xml", "w", encoding='ISO-8859-9')
f.write(xml)
f.close()