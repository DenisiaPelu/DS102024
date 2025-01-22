import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class AutoPlot:
    def __init__(self):
        pass

    def univariate_plot(self, data, variables, types):
        """
        Crea gráficos univariantes dependiendo del tipo de variable.
        
        :param data: DataFrame con los datos.
        :param variables: Lista de nombres de columnas.
        :param types: Lista de tipos de las columnas.
        """
        for var, var_type in zip(variables, types):
            if var_type == 'continuo':
                plt.figure(figsize=(10, 6))
                sns.histplot(data[var], kde=True, color='skyblue')
                plt.title(f'Histograma de {var}', fontsize=14)
                plt.xlabel(var, fontsize=12)
                plt.ylabel('Frecuencia', fontsize=12)
                plt.grid(True)
                plt.show()
            elif var_type == 'nominal' or var_type == 'ordinal':
                plt.figure(figsize=(10, 6))
                sns.countplot(data=data, x=var, palette='viridis')
                plt.title(f'Gráfico de barras de {var}', fontsize=14)
                plt.xlabel(var, fontsize=12)
                plt.ylabel('Frecuencia', fontsize=12)
                plt.grid(True)
                plt.show()
            elif var_type == 'discreto':
                plt.figure(figsize=(10, 6))
                sns.countplot(data=data, x=var, palette='coolwarm')
                plt.title(f'Gráfico de barras discretas de {var}', fontsize=14)
                plt.xlabel(var, fontsize=12)
                plt.ylabel('Frecuencia', fontsize=12)
                plt.grid(True)
                plt.show()
            elif var_type == 'fecha':
                plt.figure(figsize=(10, 6))
                data[var].dt.month.value_counts().sort_index().plot(kind='bar', color='lightcoral')
                plt.title(f'Gráfico de barras por mes para {var}', fontsize=14)
                plt.xlabel('Mes', fontsize=12)
                plt.ylabel('Frecuencia', fontsize=12)
                plt.grid(True)
                plt.show()

    def bivariate_plot(self, data, variables, types):
        """
        Crea gráficos bivariantes dependiendo de los tipos de las variables.
        
        :param data: DataFrame con los datos.
        :param variables: Lista de nombres de columnas.
        :param types: Lista de tipos de las columnas.
        """
        x_var, y_var = variables
        x_type, y_type = types

        if x_type == 'continuo' and y_type == 'continuo':
            plt.figure(figsize=(10, 6))
            sns.scatterplot(data=data, x=x_var, y=y_var, color='teal')
            plt.title(f'Gráfico de dispersión entre {x_var} y {y_var}', fontsize=14)
            plt.xlabel(x_var, fontsize=12)
            plt.ylabel(y_var, fontsize=12)
            plt.grid(True)
            plt.show()
        elif (x_type == 'continuo' and y_type == 'nominal') or (x_type == 'nominal' and y_type == 'continuo'):
            plt.figure(figsize=(10, 6))
            sns.boxplot(data=data, x=x_var, y=y_var, palette='Set2')
            plt.title(f'Gráfico de caja entre {x_var} y {y_var}', fontsize=14)
            plt.xlabel(x_var, fontsize=12)
            plt.ylabel(y_var, fontsize=12)
            plt.grid(True)
            plt.show()
        elif x_type == 'nominal' and y_type == 'nominal':
            plt.figure(figsize=(10, 6))
            sns.countplot(data=data, x=x_var, hue=y_var, palette='muted')
            plt.title(f'Gráfico de barras agrupadas entre {x_var} y {y_var}', fontsize=14)
            plt.xlabel(x_var, fontsize=12)
            plt.ylabel('Frecuencia', fontsize=12)
            plt.grid(True)
            plt.show()

    def multivariate_plot(self, data, variables, types):
        """
        Crea gráficos multivariantes dependiendo de los tipos de las variables.
        
        :param data: DataFrame con los datos.
        :param variables: Lista de nombres de columnas.
        :param types: Lista de tipos de las columnas.
        """
        if all(v_type == 'continuo' for v_type in types):
            plt.figure(figsize=(10, 6))
            sns.pairplot(data[variables], kind='scatter', palette='viridis')
            plt.title('Gráfico de dispersión múltiple', fontsize=14)
            plt.show()
        elif 'nominal' in types and 'continuo' in types:
            plt.figure(figsize=(10, 6))
            sns.catplot(data=data, x=variables[0], y=variables[1], hue=variables[2], kind='point', palette='Set1')
            plt.title(f'Gráfico de puntos entre {variables[0]} y {variables[1]} por {variables[2]}', fontsize=14)
            plt.show()