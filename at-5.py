def calcular_crescimento_populacional_while_true():
    pop_a = 80000
    taxa_a = 0.03 
    pop_b = 200000
    taxa_b = 0.015 
    print("=== Crescimento Populacional: País A vs País B (Com while True) ===")
    print(f"Início: País A = {pop_a}, País B = {pop_b}")
    print(f"Taxas: País A = {taxa_a*100:.1f}%, País B = {taxa_b*100:.1f}%")
    if taxa_a <= taxa_b:
        print("\nResultado: País A nunca alcançará B (taxa inferior ou igual).")
        return
    anos = 0
    while True:
        if pop_a >= pop_b:
            break  
        pop_a *= (1 + taxa_a)
        pop_b *= (1 + taxa_b)
        anos += 1
        if anos > 5000:
             print("\nAVISO: Limite de 5000 anos atingido. O cálculo foi interrompido.")
             break    
    if pop_a >= pop_b and anos <= 5000:
        print(f"\nApós {anos} anos, A alcança/ultrapassa B.")
        print("\nPopulação final estimada:")
        print(f"- País A: {int(pop_a):,} habitantes")
        print(f"- País B: {int(pop_b):,} habitantes")
if __name__ == "__main__":
    calcular_crescimento_populacional_while_true()