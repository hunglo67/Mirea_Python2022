def generate_groups() :
    all_groups=[]

    IVBO=[]
    for i in range(1,11):
        if i < 10:
            IVBO.append("ИВБО-0" + str(i) + "-20")
        else:
            IVBO.append("ИВБО-" + str(i) + "-20")
    all_groups.append(IVBO)
    
    IKBO = []
    for i in range(1,33):
        if i < 10:
            IKBO.append("ИКБО-0" +str(i) + "-20")
        else:
            IKBO.append("ИКБО-" +str(i) + "-20")
    all_groups.append(IKBO)
    
    INBO = []
    for i in range(1,16):
        if i < 10:
            INBO.append("ИНБО-0" +str(i) + "-20")
        else:
            INBO.append("ИНБО-" +str(i) + "-20")
    all_groups.append(INBO)
            
    IMBO = []
    for i in range(1,5):
        if i < 10:
            IMBO.append("ИМБО-0" +str(i) + "-20")
        else:
            IMBO.append("ИМБО-" +str(i) + "-20")
    all_groups.append(IMBO)
    
    for item in range(len(all_groups)):
        print(all_groups[item])

generate_groups()
