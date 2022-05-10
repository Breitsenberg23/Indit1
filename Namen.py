namen = ("Peter", "Dora", "Kevin", "Fritz", "Sarah")

def begruessung(namen):
    print("hallo, " + namen)
    print("schön dich zu sehen!")
    return

def begruessung2(namen):
    for ein_name in namen:
        print("Hallo, "  + ein_name)
        print("Schön dich zu sehen")
    return

print("Version 1")
for name in namen:
    begruessung(name)
    
print("Version 2")
begruessung2(namen)


    
