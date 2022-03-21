import re

S = '( <sect>var rima <| [q(atle_580) ;q(reso_670) ;q(vere_921) ]</sect>.\
<sect> var raqu<| [ q(teonin); q(orrema) ] </sect>. <sect> var\
xear_138 <| [ q(oranso_538) ; q(quso); q(biceis_141);q(ared_357)]\
</sect>.)'
def main(s):
    D = {}
    s = s.replace("\n", " ")
    d = re.findall(r'<sect>(.*?)<\/sect>', s)
    for i in d:
        prt = re.sub(r'\D?var', string=i, repl='')
        key = re.findall(r'\[(.*?)\]', prt)
        for j in key:
            keys = re.findall(r'\((.*?)\)',j)
        values = re.findall(r'\s?(.*?)\s?<\D?|',prt)[0]
        D[values] = keys
        print(keys)
    return D


print(main(S))
