import pulp

prob = pulp.LpProblem("Maximizacion_Perfumes_Gaermont", pulp.LpMaximize)

x_R = pulp.LpVariable("Libras_Materia_Prima", lowBound=0, cat='Continuous')
y_S = pulp.LpVariable("Onzas_Sensatez_Normal", lowBound=0, cat='Continuous')
y_SP = pulp.LpVariable("Onzas_Sensatez_Plus", lowBound=0, cat='Continuous')
y_T = pulp.LpVariable("Onzas_Sentimiento_Normal", lowBound=0, cat='Continuous')
y_TD = pulp.LpVariable("Onzas_Sentimiento_Deep", lowBound=0, cat='Continuous')

prob += 7 * y_S + 6 * y_T + 14 * y_SP + 10 * y_TD - 3 * x_R, "Utilidad_Total"

# Restricciones
prob += x_R <= 4000, "Limite_Materia_Prima"

prob += 1 * x_R + 3 * y_SP + 2 * y_TD <= 6000, "Limite_Mano_Obra"

prob += y_S + y_SP <= 3 * x_R, "Balance_Sensatez"

prob += y_T + y_TD <= 4 * x_R, "Balance_Sentimiento"

prob.solve()

print(f"Estado de la solución: {pulp.LpStatus[prob.status]}")
for v in prob.variables():
    if v.varValue > 0:
        print(f"{v.name} = {v.varValue:,.2f}")

print("-" * 30)
print(f"Utilidad Máxima (z*): ${pulp.value(prob.objective):,.2f}")