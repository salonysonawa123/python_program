import xml.etree.ElementTree as ET
import mysql.connector
import os


conn = mysql.connector.connect(user='root',
                            password='1234',
                            host='localhost',
                            database='ProductSaleData')

path = "{{path}}"               #where XML file Store 
dir_list = os.listdir(path) 
print(dir_list)
def sqldata(data1,data3):
    try:
        for i,j in data1:
            CompName = i.find('NAME').text
            RemoteCompName = i.find('REMOTECMPNAME').text
            RemoteCompState = i.find('REMOTECMPSTATE').text
            MasterId = msid
            c = conn.cursor()
            try:
                c.execute("CREATE TABLE COMPANY(MasterId VARCHAR(255), CompName VARCHAR(255), RemoteCompName VARCHAR(255),RemoteCompState VARCHAR(255),PRIMARY KEY (MasterId,CompName))")
            except:
                pass
            data_1 = """INSERT INTO COMPANY(MasterId, CompName,RemoteCompName,RemoteCompState) VALUES(%s,%s,%s,%s)"""
            c.execute(data_1, (MasterId,CompName,RemoteCompName,RemoteCompState))
            conn.commit()
    except:
        pass
    try:
        for i,j in data3:
            MasterId = msid
            ClassName = i.find('CLASSNAME').text
            VoucherName = i.find('VOUCHERTYPENAME').text
            VoucherNumber = i.find('VOUCHERNUMBER').text
            VoucherDate = i.find('DATE').text
            PsereQbySto = i.find('PSEREQBYSTO').text
            Isoptional = i.find('ISOPTIONAL').text
            IsCancelled = i.find('ISCANCELLED').text
            AlterId     = i.find('ALTERID').text
            try:
                GUID        = i.find('GUID').text
            except:
                GUID = []
            c = conn.cursor()
            try:
                c.execute("CREATE TABLE VOUCHERS (MasterId VARCHAR(255),ClassName VARCHAR(255), VoucherName VARCHAR(255), VoucherNumber VARCHAR(255), VoucherDate VARCHAR(255) , PsereQbySto VARCHAR(255),Isoptional VARCHAR(255), IsCancelled VARCHAR(255), AlterId VARCHAR(255),GUID VARCHAR(255),PRIMARY KEY (MasterId,PsereQbySto))")
            except:
                data_3 = """INSERT INTO VOUCHERS(MasterId,ClassName, VoucherName, VoucherNumber, VoucherDate, PsereQbySto,Isoptional,IsCancelled,AlterId,GUID) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
                c.execute(data_3, (MasterId,ClassName,VoucherName, VoucherNumber, VoucherDate, PsereQbySto,Isoptional,IsCancelled,AlterId,GUID))
                conn.commit()
    
    except:
        pass
   
for n in range(len(dir_list)):
    tree = ET.parse("E:\\JavaScript begins\\allfilecon\\ProdSales\\"+dir_list[n])
    # try:
    #     for elem in tree.findall('BODY/VOUCHER/LEDGERENTRIES'):
    #         elem.tag = "ALLLEDGERENTRIES"
    #         tree.write("E:\\JavaScript begins\\allfilecon\\ProdSales\\"+dir_list[n])
    # except:
    #     pass
    
    try:
        data1 = tree.findall('BODY/COMPANY/REMOTECMPINFO.LIST')
        data2 = tree.findall('BODY/VOUCHER/PSEBODYINFOAGGR')
        data3 = tree.findall('BODY/VOUCHER')
    except:
        pass

    msid = tree.find('BODY/VOUCHER/MASTERID').text

    for i, j in data2:
        MasterId = msid
        PersonNo = i.find('PSESRNO').text
        PartySto = i.find('PSEPARTYNMSTO').text
        ItemSto = i.find('PSEITEMNMSTO').text
        OrderNumSto = i.find('PSEORDERNOSTO').text
        OrderDtsSto = i.find('PSEORDERDTSTO').text
        OrderDueDts = i.find('PSEORDERDUEDTSTO').text
        DespQtySto = i.find('PSEDESPQTYSTO').text
        QtyPerBinSto = i.find('PSEQTYPERBINSTO').text
        BinQtyStoNew = i.find('PSENOOFBINQTYSTONEW').text
        PalletSto = i.find('PSENOOFPALLETSTO').text
        InvQtySto = i.find('PSENOOFINVQTYSTO').text
        ProdQtySto = i.find('PSEPRODQTYSTO').text
        RateSto = i.find('PSERATESTO').text
        
        # sql query to insert data into database
        c = conn.cursor()
        try:
            c.execute("CREATE TABLE PRODUCTSELLINFO (MasterId VARCHAR(255), PersonNo VARCHAR(255), PartySto VARCHAR(255),ItemSto VARCHAR(255) , OrderNumSto VARCHAR(255),OrderDtsSto VARCHAR(255),OrderDueDts VARCHAR(255),DespQtySto VARCHAR(255),QtyPerBinSto VARCHAR(255),BinQtyStoNew VARCHAR(255),PalletSto VARCHAR(255),InvQtySto VARCHAR(255),ProdQtySto VARCHAR(255),RateSto VARCHAR(255), PRIMARY KEY (MasterId,ItemSto))")
        except:
            pass
        try:
            data_2 = """INSERT INTO PRODUCTSELLINFO (MasterId, PersonNo,PartySto,ItemSto,OrderNumSto,OrderDtsSto,OrderDueDts,DespQtySto,QtyPerBinSto,BinQtyStoNew,PalletSto,InvQtySto,ProdQtySto,RateSto) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
            c.execute(data_2, (MasterId,PersonNo,PartySto,ItemSto,OrderNumSto,OrderDtsSto,OrderDueDts,DespQtySto,QtyPerBinSto,BinQtyStoNew,PalletSto,InvQtySto,ProdQtySto,RateSto))
            conn.commit()
            sqldata(data1,data3)
        except:
            pass