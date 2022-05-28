def arithmetic_arranger(ops, pres = False):
    arranged_problems = ''
    
    if len(ops) > 5:
        return "Error: Too many problems."
    
    # the 4 lines to print
    line1 = ""  #linea con los primeros operadores
    line2 = ""  #linea con los segundos operadores
    line3 = ""  #linea con los guiones
    line4 = ""  #linea con los resultados
    
    for op in ops:
        #do all for each op
        error_op = False
        suma, resta, place, error_op = busca_op(op)
        if error_op == True:
            return "Error: Operator must be '+' or '-'."

        try:
            op1 = int(op[:place])
            op2 = int(op[place+3:])
        except:
            return "Error: Numbers must only contain digits."
        
        if op1 > 9999 or op2 > 9999: #solo positivos or op1 < -9999 or op2 < -9999:
            return "Error: Numbers cannot be more than four digits."
            
        result = do_op(suma, resta, op1, op2)
        line1, line2, line3, line4 = fill_lines(line1, line2, line3, line4, op1, op2, result, suma)

    arranged_problems += line1.rstrip() + "\n" + line2.rstrip() + "\n" + line3.rstrip()
    if pres == True:    
        arranged_problems += "\n" + line4.rstrip()

    return arranged_problems

def fill_lines(line1, line2, line3, line4, op1, op2, result, suma):
    #find de biggest number
    espacios = 0
    for i in [op1, op2]:
        if len(str(i)) > espacios:   
            espacios = len(str(i))
    max_espacios = espacios + 2
    line3 = line3 + "-" * max_espacios + " " * 4
    line1 = line1 + " " * (max_espacios - len(str(op1))) + str(op1) + " " * 4
    if suma == True:
        line2 = line2 + "+" + " " * (max_espacios - 1 - len(str(op2))) + str(op2) + " " * 4
    else:
        line2 = line2 + "-" + " " * (max_espacios - 1 - len(str(op2))) + str(op2) + " " * 4
    line4 = line4 + " " * (max_espacios - len(str(result))) + str(result) + " " * 4 #la linea 4 está poniendo siempre los espacios al final
    return line1, line2, line3, line4

def do_op(suma, resta, op1, op2):
    if suma == True:
        return op1 + op2
    else:
        return op1 - op2
    
def busca_op(op):
    suma = False
    resta = False
    place = None
    if " + " in op:
        place = op.find(" + ")
        suma = True
    elif " - " in op:
        place = op.find(" - ")
        resta = True
    else:
        return suma, resta, place, True    
    return suma, resta, place, False