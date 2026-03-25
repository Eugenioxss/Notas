import pulp

# 1. Crear el problema de maximización
prob = pulp.LpProblem("Max_Utilidad_Productos", pulp.LpMaximize)

# 2. Variables de decisión (Enteras x >= 0)
x_1 = pulp.LpVariable("x1", lowBound=0, cat='Integer') # Producto 1
x_2 = pulp.LpVariable("x2", lowBound=0, cat='Integer') # Producto 2

# 3. Función Objetivo
prob += 12*x_1 + 4*x_2, "Utilidad_Total"

# 4. Restricciones
prob += x_1 + 2*x_2 <= 800, "Limite1"
prob += x_1 + 3*x_2 <= 600, "Limite2"
prob += 2*x_1 + 3*x_2 <= 2000, "Horas"

# 5. Resolver el problema
prob.solve()

# 6. Mostrar resultados
print(f"Estado del Solver: {pulp.LpStatus[prob.status]}")
print(f"Producir Producto 1 (x1): {pulp.value(x_1)}")
print(f"Producir Producto 2 (x2): {pulp.value(x_2)}")
print(f"Utilidad Máxima (z): ${pulp.value(prob.objective)}")