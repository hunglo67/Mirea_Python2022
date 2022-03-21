import re

S = "<section> do global beri <== #('raanle_758' ,'isle_99') end,do global\
erve<== #('atre_667' , 'isceon_951','bice_616', 'esed') end, do global\
isarus_680<==#( 'ener_91' ,'dilear_686' ) end, </section>"
def main1(s):
    A=[]
    B=[]
    D = {}
    s = s.replace("\n", " ")
    d = re.findall(r'<section>(.*?)<\/section>', s)
    for i in d:
         prt1 = re.sub(r'\D?do',string = i , repl = '')
         prt2 = re.sub(r'\D?end',string = prt1, repl ='')
         prt3 = re.sub(r'\D?global', string = prt2 , repl = '')
         key = re.findall(r'\((.*?)\)',prt3)
         for item_key in key:
                itemk = item_key.replace('\'','')
                itemd = itemk.split(",")
                B.append(itemd)
         values = [x.replace(' ','') for x in re.findall(r'\s?(.*?)\s?\D?#',prt3)]
         for i in values:
             valuess4 =  re.findall("\w+\<=+",i)
             for l in valuess4:
                 valuess5 = re.sub(r'\D?=', string = l , repl = '')
                 A.append(valuess5)      
    dictionary = dict(zip(A, B))
    return dictionary
    
print(main1(S))
    
