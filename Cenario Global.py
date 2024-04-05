
username = 'YourTradingViewUserName'
password = 'YourTradingViewPassword'

# É possível coletar os dados sem fornecer dados de usuário e senha


from main import TvDatafeed,Interval

tv = TvDatafeed(username,password)

import yfinance as yf
import pandas as pd
import numpy as np
import seaborn as srn
import statistics as sts
import os
from datetime import date

os.chdir('\\\lupin\\CODEN\PBI - Mercado Global')

verticesbr= ['BR09MY','BR01Y','BR02Y','BR03Y','BR05Y','BR08Y','BR10Y']
verticesus= ['US01MY','US03MY','US06MY','US01Y','US02Y','US03Y','US05Y','US07Y','US10Y','US30Y']
verticescn=['CN01Y','CN02Y','CN03Y','CN05Y','CN07Y','CN10Y']
verticeseu=['EU01MY','EU03MY','EU06MY','EU09MY','EU01Y','EU02Y','EU03Y','EU05Y','EU07Y','EU10Y']
verticesin=['IN01Y','IN02Y','IN05Y','IN10Y']
verticesjp=['JP01Y','JP02Y','JP05Y','JP10Y']
verticesde=['DE01MY','DE03MY','DE06MY','DE09MY','DE01Y','DE02Y','DE03Y','DE05Y','DE07Y','DE10Y']


verticesbr_anos = [0.75,1,2,3,5,8,10]
verticesus_anos= [0.08,0.25,0.5,1,2,3,5,7,10,30]
verticescn_anos=[1,2,3,5,7,10]
verticeseu_anos=[0.08,0.25,0.5,0.75,1,2,3,5,7,10]
verticesin_anos=[1,2,5,10]
verticesjp_anos=[1,2,5,10]
verticesde_anos=[0.08,0.25,0.5,0.75,1,2,3,5,7,10]


#### Busca o histórico dos juros e formata o DataFrame para incluir o nome do País e unificar o nome das colunas
#### Os dados são coletados em um frame de cotações diárias e tenta buscar até 750 dias limitado à base existente


# definição de parametros de busca

intervalo = Interval.in_daily
qtde_intervalos = 10200

painelBR = pd.DataFrame()
for i in verticesbr:
  painelBR[i] = tv.get_hist(i,'TVC',intervalo,qtde_intervalos)['close']
#painelBR = painelBR.dropna()
painelBR.columns = verticesbr
painelBR2 = painelBR
painelBR2.columns = verticesbr_anos
painelBR2 = painelBR2.melt(ignore_index=False)
painelBR2.columns = ['Venc', 'Taxa']
painelBR2 = painelBR2[['Taxa',"Venc"]]
painelBR2['País'] = 'Brasil'
painelBR['País'] = 'Brasil'

painelUS = pd.DataFrame()
for i in verticesus:
  painelUS[i] = tv.get_hist(i,'TVC',intervalo,qtde_intervalos)['close']
#painelUS = painelUS.dropna()
painelUS.columns = verticesus
painelUS2 = painelUS
painelUS2.columns = verticesus_anos
painelUS2 = painelUS2.melt(ignore_index=False)
painelUS2.columns = ['Venc', 'Taxa']
painelUS2 = painelUS2[['Taxa',"Venc"]]
painelUS2['País'] = 'Estados Unidos'
painelUS['País'] = 'Estados Unidos'

painelCN = pd.DataFrame()
for i in verticescn:
  painelCN[i] = tv.get_hist(i,'TVC',intervalo,qtde_intervalos)['close']
#painelCN = painelCN.dropna()
painelCN.columns = verticescn
painelCN2 = painelCN
painelCN2.columns = verticescn_anos
painelCN2 =painelCN2.melt(ignore_index=False)
painelCN2.columns = ['Venc', 'Taxa']
painelCN2 = painelCN2[['Taxa',"Venc"]]
painelCN2['País'] = 'China'
painelCN['País'] = 'China'

painelEU = pd.DataFrame()
for i in verticeseu:
  painelEU[i] = tv.get_hist(i,'TVC',intervalo,qtde_intervalos)['close']
#painelEU = painelEU.dropna()
painelEU.columns = verticeseu
painelEU2 = painelEU
painelEU2.columns = verticeseu_anos
painelEU2 = painelEU2.melt(ignore_index=False)
painelEU2.columns = ['Venc', 'Taxa']
painelEU2 = painelEU2[['Taxa',"Venc"]]
painelEU2['País'] = 'Zona do Euro'
painelEU['País'] = 'Zona do Euro'

painelIN = pd.DataFrame()
for i in verticesin:
  painelIN[i] = tv.get_hist(i,'TVC',intervalo,qtde_intervalos)['close']
#painelIN = painelIN.dropna()
painelIN.columns = verticesin
painelIN2 = painelIN
painelIN2.columns = verticesin_anos
painelIN2 = painelIN2.melt(ignore_index=False)
painelIN2.columns = ['Venc', 'Taxa']
painelIN2 = painelIN2[['Taxa',"Venc"]]
painelIN2['País'] = 'India'
painelIN['País'] = 'India'

painelJP = pd.DataFrame()
for i in verticesjp:
  painelJP[i] = tv.get_hist(i,'TVC',intervalo,qtde_intervalos)['close']
#painelJP = painelJP.dropna()
painelJP.columns = verticesjp
painelJP2 = painelJP
painelJP2.columns = verticesjp_anos
painelJP2 = painelJP2.melt(ignore_index=False)
painelJP2.columns = ['Venc', 'Taxa']
painelJP2 = painelJP2[['Taxa',"Venc"]]
painelJP2['País'] = 'Japao'
painelJP['País'] = 'Japao'

painelDE = pd.DataFrame()
for i in verticesde:
  painelDE[i] = tv.get_hist(i,'TVC',intervalo,qtde_intervalos)['close']
#painelDE = painelDE.dropna()
painelDE.columns  = verticesde
painelDE2 = painelDE
painelDE2.columns = verticesde_anos
painelDE2 = painelDE2.melt(ignore_index=False)
painelDE2.columns = ['Venc', 'Taxa']
painelDE2 = painelDE2[['Taxa',"Venc"]]
painelDE2['País'] = 'Alemanha'
painelDE['País'] = 'Alemanha'

curva_paises = pd.DataFrame()
curva_paises = pd.concat([painelBR2,painelCN2,painelUS2,painelEU2,painelIN2,painelDE2,painelJP2],axis=0, join = 'outer',ignore_index=False)
curva_paises.columns = ['Taxa', 'Venc', 'Pais']
curva_paises.to_csv('Curva Paises.csv')


jurosglb = pd.concat([painelBR,painelUS,painelCN,painelEU,painelIN,painelDE,painelJP])

jurosglb.columns = [ '3 meses' , '1 Ano', '2 Anos', '3 Anos',
                     '5 Anos', '8 Anos', '10 Anos', 'Pais',
                       '1 mes', '3 meses', '6 meses', '7 Anos','30 Anos']

jurosglb['Diff 10 - 2'] = jurosglb['10 Anos'] -  jurosglb['2 Anos']

jurosglb.index = jurosglb.index.strftime('%m/%d/%Y')

jurosglb.dropna( subset = ['Pais'], inplace=True)

jurosglb.to_csv('Juros Global Consolidado.csv')


#Busca de contratos ativos de DI Futuro

di = tv.search_symbol('DI1')


##Isolando resultados da consulta de contratos ativos 

a = pd.DataFrame(di[0]['contracts'][2:])
# a = a.tolist()
# a = pd.DataFrame0(a)

contratosdi = a[['symbol','description']][2:]
contratosdi.columns = ['Contrato','Vencimento']

list_di = contratosdi['Contrato'].tolist()
list_di.remove('DI1M2024')


curva_juros = pd.DataFrame()
for i in list_di:
  #print(i)

  curva_juros[i] = tv.get_hist(i,'',Interval.in_daily,7)['close']


####################################################################################
### REMOVE O CONTRATO QUE DEU PROBLEMA SE FOR O CASO
####################################################################################
c = contratosdi['Vencimento'].to_list()
c.remove('Jun 2024')


a = curva_juros.T
a = a.assign(Vencimento = c)
a.columns = ['D-6','D-5','D-4','D-3','D-2','D-1','Dia Atual', 'Vencimento']
a.to_csv ('Curva de Juros.csv')


moedasyf = ['BRL=X','AUD=X','CAD=X','CLP=X','COP=X','NZD=X','ZAR=X','INR=X','MXN=X','TRY=X','CNY=X','EUR=X','DX=F']

moedaspainelyf = pd.DataFrame()


for i in moedasyf:
  moedaspainelyf[i] = yf.download(i,'2012-01-01').Close

moedaspainelyf.columns = ['BRL','AUD','CAD','CLP','COP','NZD','ZAR','INR','MXN','TRY','CNY','EUR','DXY']


cesta  =pd.DataFrame()

cesta['BRL'] = moedaspainelyf.BRL

cesta['Ind GEMAC'] = 0.35*(moedaspainelyf.AUD**0.1992) * (moedaspainelyf.CAD**0.2427)* ((moedaspainelyf.CLP / 100)**0.1964) * ((moedaspainelyf.COP / 1000)**0.3311) * (moedaspainelyf.NZD**0.1753) * (moedaspainelyf.ZAR**0.2049)* ((moedaspainelyf.INR / 10)**0.3427) * ((moedaspainelyf.MXN / 10)**0.2622)* (moedaspainelyf.TRY**0.0532)

### Retirada de outliers
outlier = 0.8*cesta['Ind GEMAC'].shift(1)
cesta['Ind GEMAC'] = cesta.loc[cesta['Ind GEMAC']> outlier,'Ind GEMAC'] 
cesta = cesta.dropna()

moedas  =pd.DataFrame()
moedas= moedaspainelyf[['BRL','AUD','CAD','CLP','COP','NZD','ZAR','INR','MXN','TRY','CNY','EUR','DXY']]
moedas['Ind GEMAC'] = cesta['Ind GEMAC']


#x = moedas.values.tostring()
moedas.index = moedas.index.strftime('%m/%d/%Y')


moedas.columns = ['BRASIL', 'AUSTRALIA', 'CANADA', 'CHILE', 'COLOMBIA', 'NOVA ZELANDIA', 'AFRICA DO SUL', 'INDIA', 'MEXICO', 'TURQUIA',
       'CHINA', 'EURO', 'Ind DOLAR', 'Ind GEMAC']

moedas = moedas.dropna()

moedas.to_csv('Moedas.csv')

retorno_moedas = moedas.pct_change().dropna()

retorno_moedas.to_csv('Moedas retorno.csv')

#procedimento para empilhar todas as moedas na mesma coluna

moedas_emp = moedas.melt(ignore_index = False)
moedas_emp [ 'Variacao'] = moedas_emp.groupby('variable').pct_change()
moedas_emp.dropna(inplace = True)
moedas_emp = moedas_emp[['value','Variacao','variable']]
moedas_emp.columns = ['Cotacao', 'Variacao', 'Moeda']
moedas_emp.to_csv('Moedas Empilhado.csv')


indices = ['SPX','DJI','NDX','HSI','EU50','DAX','CAC40','UK100','NI225','IBOV']

from datetime import datetime

spx = pd.DataFrame()
spx['SPX'] = tv.get_hist('SPX','',Interval.in_daily,12600).close
spx['Data'] = spx.index.strftime('%m/%d/%Y')
spx.index = spx.index.strftime('%m/%d/%Y')

dji = pd.DataFrame()
dji['DJI'] = tv.get_hist('DJI','',Interval.in_daily,12600).close
dji['Data'] = dji.index.strftime('%m/%d/%Y')
dji.index = dji.index.strftime('%m/%d/%Y')

ndx = pd.DataFrame()
ndx['NDX'] = tv.get_hist('NDX','',Interval.in_daily,1260).close
ndx['Data'] = ndx.index.strftime('%m/%d/%Y')
ndx.index = ndx.index.strftime('%m/%d/%Y')

hsi = pd.DataFrame()
hsi['HSI'] = tv.get_hist('HSI','',Interval.in_daily,12600).close
hsi['Data'] = hsi.index.strftime('%m/%d/%Y')
hsi.index = hsi.index.strftime('%m/%d/%Y')

szse = pd.DataFrame()
szse['SZSE']= tv.get_hist('399001','',Interval.in_daily,12600).close
szse['Data'] = szse.index.strftime('%m/%d/%Y')
szse.index = szse.index.strftime('%m/%d/%Y')

eu50 = pd.DataFrame()
eu50['EU50'] = tv.get_hist('EU50','',Interval.in_daily,12600).close
eu50['Data'] = eu50.index.strftime('%m/%d/%Y')
eu50.index = eu50.index.strftime('%m/%d/%Y')

dax = pd.DataFrame()
dax['DAX'] = tv.get_hist('DAX','',Interval.in_daily,12600).close
dax['Data'] = dax.index.strftime('%m/%d/%Y')
dax.index = dax.index.strftime('%m/%d/%Y')

cac40 = pd.DataFrame()
cac40['CAC40'] = tv.get_hist('CAC40','',Interval.in_daily,12600).close
cac40['Data'] = cac40.index.strftime('%m/%d/%Y')
cac40.index = cac40.index.strftime('%m/%d/%Y')

uk100 = pd.DataFrame()
uk100['FTSE100'] = tv.get_hist('UK100','',Interval.in_daily,12600).close
uk100['Data'] = uk100.index.strftime('%m/%d/%Y')
uk100.index = uk100.index.strftime('%m/%d/%Y')

ni225 = pd.DataFrame()
ni225['Nikkei'] = tv.get_hist('NI225','',Interval.in_daily,12600).close
ni225['Data'] = ni225.index.strftime('%m/%d/%Y')
ni225.index = ni225.index.strftime('%m/%d/%Y')

ibov = pd.DataFrame()
ibov['IBOV']= tv.get_hist('IBOV','',Interval.in_daily,12600).close
ibov['Data'] = ibov.index.strftime('%m/%d/%Y')
ibov.index = ibov.index.strftime('%m/%d/%Y')   


indpaine2 = pd.DataFrame()
indpaine2['IBOV']= ibov['IBOV']
indpaine2['Japao'] = ni225['Nikkei']
indpaine2['Franca'] = cac40['CAC40']
indpaine2['Alemanha'] = dax['DAX']
indpaine2['UK'] = uk100['FTSE100']
indpaine2['EURO'] = eu50['EU50']
indpaine2['Hong kong']  = hsi['HSI']
indpaine2['Shenzhen']  = szse['SZSE']
indpaine2['SP500'] = spx['SPX']
indpaine2['DowJones'] = dji['DJI']
indpaine2['Nasdaq'] = ndx['NDX']
indpaine2.index.name = 'Data'
indpaine2.fillna(method='ffill', inplace = True)

indpaine2.to_csv('Indices.csv')

indpaine_long = indpaine2.melt(ignore_index = False)
indpaine_long.columns = ['Indices', 'Cotacao']
indpaine_long.to_csv('Indices Empilhados.csv')

indices_norm = indpaine2.dropna() /indpaine2.dropna().iloc[0]
indices_norm.to_csv ('Indices Retorno Normalizado.csv')
#indices_norm.plot(figsize=(30,11))

retornos_indices = indpaine2.pct_change()

vix = pd.DataFrame()
vix['VIX']= tv.get_hist('VIX','',Interval.in_daily,12600).close
vix['Data'] = vix.index.strftime('%m/%d/%Y')
vix.index = vix.index.strftime('%m/%d/%Y')

indices_desvpad = retornos_indices.rolling(90).std()
indices_desvpad['VIX'] = vix['VIX']

indices_desvpad
indices_desvpad.to_csv('Volatilidade 90 Dias.csv')

pais = ['USCIR','EUCIR','CNCIR','BRCIR','MXCIR','JPCIR','DECIR','GBCIR','FRCIR','RUCIR','AUCIR']

cpi = pd.DataFrame()

for i in pais:
    cpi[i] = tv.get_hist(i,'',n_bars=24).close

cpi.columns = ['Estados Unidos', 'Europa', 'China', 'Brasil', 'Mexico', 'Japao', 'Alemanha', 'Reino Unido',
       'Franca', 'Russia', 'Australia']
cpi.index = cpi.index.strftime('%m/%d/%Y')

cpi.to_csv('CPI.csv')

commod_dict = {'DJCIGC': 'OURO',
 'DJCISI': 'PRATA',
 'DJCIIK': 'NIQUEL',
 'DJCIEN': 'ENERGIA',
 'DJCIGR': 'GRÃOS',
 'DJCISB': 'AÇUCAR',
 'DJCICC': 'CACAU',
 'DJCIAGC': 'AGRICULTURA',
 }

commod_dict2 = { 'AW1!' : 'CBOM',
 'NG1!': 'GÁS NATURAL',
 'TIO1!': 'FERRO',
 'HG1!': 'COBRE'}

commod_dict3 = {'UKOIL': 'PETROL BRENT'}

commod_dict4 = {'ZS1!' : 'SOJA'}

cesta_commodities = pd.DataFrame()

for i in list(commod_dict.keys()):
    print(i)
    cesta_commodities[i] = tv.get_hist(i,'',Interval.in_daily, 1260).close

cesta_commodities['Data'] = cesta_commodities.index.strftime('%m/%d/%Y')
cesta_commodities.index = cesta_commodities.index.strftime('%m/%d/%Y')  
cesta_commodities = cesta_commodities.set_index(cesta_commodities['Data'])
del cesta_commodities['Data']

cesta_commodities.columns = commod_dict.values()

cesta_commodities2 = pd.DataFrame()

for i in list(commod_dict2.keys()):
    print(i)
    cesta_commodities2[i] = tv.get_hist(i,'',Interval.in_daily, 1260).close

cesta_commodities2['Data'] = cesta_commodities2.index.strftime('%m/%d/%Y')
cesta_commodities2.index = cesta_commodities2.index.strftime('%m/%d/%Y')  
cesta_commodities2 = cesta_commodities2.set_index(cesta_commodities2['Data'])
del cesta_commodities2['Data']

cesta_commodities2.columns = commod_dict2.values()

cesta_commodities3 = pd.DataFrame()

for i in list(commod_dict3.keys()):
    print(i)
    cesta_commodities3[i] = tv.get_hist(i,'',Interval.in_daily, 1260).close

cesta_commodities3['Data'] = cesta_commodities3.index.strftime('%m/%d/%Y')
cesta_commodities3.index = cesta_commodities3.index.strftime('%m/%d/%Y')  
cesta_commodities3 = cesta_commodities3.set_index(cesta_commodities3['Data'])
del cesta_commodities3['Data']

cesta_commodities3.columns = commod_dict3.values()

cesta_commodities4 = pd.DataFrame()

for i in list(commod_dict4.keys()):
    print(i)
    cesta_commodities4[i] = tv.get_hist(i,'',Interval.in_daily, 1260).close

cesta_commodities4['Data'] = cesta_commodities4.index.strftime('%m/%d/%Y')
cesta_commodities4.index = cesta_commodities4.index.strftime('%m/%d/%Y')  
cesta_commodities4 = cesta_commodities4.set_index(cesta_commodities4['Data'])
del cesta_commodities4['Data']

cesta_commodities4.columns = commod_dict4.values()

commmodity_painel = pd.DataFrame()

commmodity_painel = cesta_commodities.merge(cesta_commodities2, how='left', on = 'Data')
commmodity_painel = commmodity_painel.merge(cesta_commodities3, how= 'left', on= 'Data')
commmodity_painel = commmodity_painel.merge(cesta_commodities4, how= 'left', on= 'Data')


cesta_commodities =commmodity_painel.dropna()
cesta_commodities.to_csv('Cesta Commodities.csv')

a = list(cesta_commodities.index)
b = list(cesta_commodities.columns)

commodities_emp = pd.DataFrame()
provisoria = pd.DataFrame()

for i in range(len(b)):
    provisoria['Data'] = cesta_commodities[b[i]].index
    provisoria['Cotação'] = cesta_commodities[b[i]].values
    provisoria['Commodity'] = b[i]


    commodities_emp = pd.concat([commodities_emp,provisoria],ignore_index=True)

commodities_emp.set_index('Data')
commodities_emp.to_csv('Commodities Empilhado.csv')