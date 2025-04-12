def fatorial(numero):
    if(numero >= 0):
        if(numero == 0):
            return 1
        else:
            return numero * fatorial(numero - 1)
        

def combinacao_simples(n, p):
    if(n >= 0 and p >= 0):
        if(n >= p):
            return fatorial(n) / fatorial(p) * fatorial(n - p)