import pulp

# ¡A facturar se ha dicho!
prob = pulp.LpProblem("Maximizacion_Inversiones_Fabulosas", pulp.LpMaximize)

# Variables de los proyectos (¡Dinero continuo, obvio!)
x1 = pulp.LpVariable("Inv_P1", lowBound=0, cat='Continuous')
x2 = pulp.LpVariable("Inv_P2", lowBound=0, cat='Continuous')
x3 = pulp.LpVariable("Inv_P3", lowBound=0, cat='Continuous')
x4 = pulp.LpVariable("Inv_P4", lowBound=0, cat='Continuous')

# Variables del banco (rendimiento de 6.5% = multiplicarlo por 1.065 cada año)
b1 = pulp.LpVariable("Banco_Año1", lowBound=0, cat='Continuous')
b2 = pulp.LpVariable("Banco_Año2", lowBound=0, cat='Continuous')
b3 = pulp.LpVariable("Banco_Año3", lowBound=0, cat='Continuous')
b4 = pulp.LpVariable("Banco_Año4", lowBound=0, cat='Continuous')

# Función Objetivo: Todo lo que cosechamos en el Año 5
prob += 1.2 * x1 + 1.3 * x2 + 0.8 * x3 + 0.95 * x4 + 1.065 * b4, "Dinero_Total_Año_5"

# Restricciones (Nodos de equilibrio de flujo de efectivo por año)
prob += x1 + x2 + x4 + b1 == 10000, "Flujo_Año_1"
prob += 0.5 * x1 + 0.6 * x2 + 0.4 * x4 + 1.065 * b1 == x3 + b2, "Flujo_Año_2"
prob += 0.3 * x1 + 0.2 * x2 + 0.8 * x3 + 0.6 * x4 + 1.065 * b2 == b3, "Flujo_Año_3"
prob += 1.8 * x1 + 1.5 * x2 + 1.9 * x3 + 1.8 * x4 + 1.065 * b3 == b4, "Flujo_Año_4"

# ¡A resolver!
prob.solve()

# El chisme de los resultados
print(f"Estado de la solución: {pulp.LpStatus[prob.status]} ✨")
for v in prob.variables():
    if v.varValue > 0:
        print(f"{v.name} = ${v.varValue:,.2f}")

print("-" * 30)
print(f"Dinero Final Máximo (z*): ${pulp.value(prob.objective):,.2f} 💅")