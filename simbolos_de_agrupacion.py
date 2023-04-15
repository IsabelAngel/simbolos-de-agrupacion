# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 17:53:08 2023

@author: ASUS
"""

def verificar_llaves(llave):
    if llave[0] == ")" or llave[0] == "]" or llave[0] == "}":
        return False
    elif len(llave) % 2 != 0:
        return False
    else:
        for caracter in range(1,len(llave)):
            if llave[caracter] == ")":
                if llave[caracter-1] == "(":
                    llave= llave[caracter-1:caracter+1] + llave[:caracter-1] + llave[caracter+1:]
                else:
                    return False
            elif llave[caracter] == "]":
                if llave[caracter-1] == "[":
                    llave= llave[caracter-1:caracter+1] + llave[:caracter-1] + llave[caracter+1:]
                else:
                    return False
            elif llave[caracter] == "}":
                if llave[caracter-1] == "{":
                    llave= llave[caracter-1:caracter+1] + llave[:caracter-1] + llave[caracter+1:]
                else:
                    return False
            else:
                continue
        return True
                

x= "[][{](})"
y="[[(({()}))]]{()}[({})]" 
z="]["
a= "([)]"
b= '{'
c= '{[]}'
d= '(]'
e="([]"
print(verificar_llaves(b))
                
                
            
# llave="{[()]}"
# for i in range(1,len(llave)+1):
#     print(i)
#     if llave[i] == "}":        
#         llave= llave[i-1:i+1] + llave[:i-1] + llave[i+1:]
#     else:
#         continue
# print(llave)



