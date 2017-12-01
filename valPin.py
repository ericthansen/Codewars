
def validate_pin(pin):
    if ((len(pin)==6 or len(pin)==4)):
        tflag=0
        for j in range(0,len(pin),1):
            if ((pin[j])>0 and (pin[j])<0):
                return True
            else:
                return False
        else:
            return False
    else:
        return False
    #return true or false

print(validate_pin('abcd'))