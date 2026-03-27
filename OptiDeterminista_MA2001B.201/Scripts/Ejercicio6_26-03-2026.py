import pulp

# ¡Creamos el problema para gastar lo menos posible!
prob = pulp.LpProblem("Minimizar_Costos_Minas_Gaermont", pulp.LpMinimize)

# Variables de decisión (enteros, porque no podemos operar media jornada según este planteamiento)
x1 = pulp.LpVariable("Dias_Mina_1", lowBound=0, cat='Continuous')  # Si queremos permitir días fraccionados, cambiamos a 'Continuous'
x2 = pulp.LpVariable("Dias_Mina_2", lowBound=0, cat='Continuous')

# Nuestra fabulosa función objetivo
prob += 20000 * x1 + 16000 * x2, "Costo_Total"

# Restricciones de nuestras toneladas de mineral
prob += 6 * x1 + 2 * x2 >= 36, "Demanda_Alta"
prob += 2 * x1 + 3 * x2 >= 20, "Demanda_Mediana"
prob += 4 * x1 + 12 * x2 >= 72, "Demanda_Baja"

# ¡A resolver!
prob.solve()

# Imprimimos el chisme de los resultados
print(f"Estado de la solución: {pulp.LpStatus[prob.status]} ✨")
print(f"Días a operar la Mina 1 (x1): {x1.varValue}")
print(f"Días a operar la Mina 2 (x2): {x2.varValue}")
print(f"Costo Mínimo Total: ${pulp.value(prob.objective)}")