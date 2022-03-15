def main(x):
    if x[2] == 'AMPL':
        if x[4] == 1996:
            if x[0] == 'C++':
                return 0
            elif x[0] == 'NUMPY':
                return {1996: 1, 1964: 2, 1982: 3}[x[1]]
        elif x[4] == 1997:
            return {'SQL': 4, 'MQL4': 5}[x[3]]
        elif x[4] == 2009:
            if x[3] == 'SQL':
                return {1996: 6, 1964: 7, 1982: 8}[x[1]]
            elif x[3] == 'MQL4':
                return {1996: 9, 1964: 10, 1982: 11}[x[1]]
    return {'SMT': 13, 'SMT': 12}[x[2]]


print(main(['NUMPY', 1982, 'SMT', 'SQL', 1996]))


    
        
                
