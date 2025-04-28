
import pandas as pd

# Cargar el archivo (ajusta la ruta si hace falta)
df = pd.read_csv("../data/mdi_detenidosaprehendidos_pm_2019_2024.csv", sep=';')

# Ver las columnas del archivo
print(df.columns)
print(df.head())
print(df.info())
print(df.describe(include='all'))
print(df['ESTADO_CIVIL'].value_counts())
# Filtrar personas casadas
casados = df[df['ESTADO_CIVIL'] == 'CASADO/A']

# Contar por tipo (detenido o aprehendido)
conteo_tipo = casados['TIPO'].value_counts()

print(conteo_tipo)

import matplotlib.pyplot as plt

conteo_tipo.plot(kind='bar', color=['orange', 'purple'])
plt.title("Personas Casadas por Tipo de Aprehensión")
plt.xlabel("Tipo")
plt.ylabel("Cantidad")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

solteros = df[df['ESTADO_CIVIL'] == 'SOLTERO/A']

conteo_tipos = solteros['TIPO'].value_counts()

print(conteo_tipos)

conteo_tipos.plot(kind='bar', color=['orange', 'purple'])
plt.title("Personas Solteras por Tipo de Aprehensión")
plt.xlabel("Tipo")
plt.ylabel("Cantidad")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

tabla = pd.crosstab(df['ESTADO_CIVIL'], df['TIPO'])
print(tabla)

from scipy.stats import chi2_contingency
chi2, p, dof, expected = chi2_contingency(tabla)
print(f"Chi-cuadrado: {chi2}")
print(f"p-valor: {p}")
print(f"Grados de libertad: {dof}")

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Tu tabla de datos (ajústala si necesitas)
datos = {
    'ESTADO_CIVIL': ['CASADO/A', 'DIVORCIADO/A', 'SE DESCONOCE', 'SOLTERO/A', 'UNION DE HECHO', 'VIUDO/A'],
    'APREHENDIDO': [51766, 14887, 15200, 263043, 3253, 1406],
    'DETENIDO': [32713, 15297, 2525, 87733, 1081, 943]
}

df = pd.DataFrame(datos)

# Convertimos el DataFrame a formato 'largo' (para seaborn)
df_melt = df.melt(id_vars='ESTADO_CIVIL', value_vars=['APREHENDIDO', 'DETENIDO'],
                  var_name='TIPO', value_name='CANTIDAD')

# Crear gráfico
plt.figure(figsize=(12, 6))
sns.barplot(data=df_melt, x='ESTADO_CIVIL', y='CANTIDAD', hue='TIPO')

plt.title('Tipo de Aprehensión por Estado Civil')
plt.xlabel('Estado Civil')
plt.ylabel('Cantidad de Personas')
plt.xticks(rotation=45)
plt.legend(title='Tipo de Aprehensión')
plt.tight_layout()
plt.show()

df_limpio = df[['ESTADO_CIVIL', 'APREHENDIDO', 'DETENIDO']]  # columnas que te interesan

df_limpio.to_csv('../data/datos_limpios.csv', index=False)

