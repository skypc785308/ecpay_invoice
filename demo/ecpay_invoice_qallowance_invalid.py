#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ecpay_invoice.ecpay_main import *

ecpay_invoice = EcpayInvoice()

# 2.寫入基本介接參數
ecpay_invoice.Invoice_Method = 'ALLOWANCE_VOID_SEARCH'
ecpay_invoice.Invoice_Url = 'https://einvoice-stage.ecpay.com.tw/Query/AllowanceInvalid'
ecpay_invoice.MerchantID = '2000132'
ecpay_invoice.HashKey = 'ejCk326UnaZWKisg'
ecpay_invoice.HashIV = 'q9jcZX8Ib9LM8wYk'

# 3.寫入發票相關資訊
ecpay_invoice.Send['InvoiceNo'] = 'FY10004005'
ecpay_invoice.Send['AllowanceNo'] = '2018071615286810'

# 4. 送出
aReturn_Info = ecpay_invoice.Check_Out()
print aReturn_Info
print aReturn_Info['RtnMsg']
