import pulp

# 1. Crear el problema de maximización
prob = pulp.LpProblem("Max_Utilidad_Autos", pulp.LpMaximize)

# 2. Variables de decisión (Enteras y >= 0)
x = pulp.LpVariable("x", lowBound=0, cat='Integer') # Automóviles
y = pulp.LpVariable("y", lowBound=0, cat='Integer') # Vagonetas

# 3. Función Objetivo
prob += 3000*x + 4000*y, "Utilidad_Total"

# 4. Restricciones
prob += x <= 300, "Limite_Autos"
prob += y <= 200, "Limite_Vagonetas"
prob += 2*x + 3*y == 900, "Horas_Taller"

# 5. Resolver el problema
prob.solve()

# 6. Mostrar resultados
print(f"Estado del Solver: {pulp.LpStatus[prob.status]}")
print(f"Vender Automóviles (x): {pulp.value(x)}")
print(f"Vender Vagonetas (y): {pulp.value(y)}")
print(f"Utilidad Máxima (z): ${pulp.value(prob.objective)}")