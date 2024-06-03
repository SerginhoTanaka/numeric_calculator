from flask import Flask, render_template, request

app = Flask(__name__)
#jogar no replit
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        num_values = int(request.form['num_values'])
        x_value = request.form['x_value']
        values = []
        for i in range(1, num_values + 1):
            value = request.form.get(f'xy_values_{i}')
            if value:
                values.append(value)
        tuples_array = []
        for value in values:
            x, y = map(float, value.split(','))
            tuples_array.append((x, y))
        print(tuples_array)
        print(num_values, "teste")
        diferences = divided_diferences(tuples_array)
        result = newton_interpolation(float(x_value), tuples_array, diferences)
            
        return render_template('index.html', result=result)
    return render_template('index.html')

def divided_diferences(points):
    """ 
    Recebe uma lista de tuplas (x,y) e retorna uma lista de coeficientes para o polinômio interpolador de Newton.
    Sendo o coeficiente 0 o valor de y0, o coeficiente 1 a diferença dividida de y0 e y1
    e assim por diante.
    O coeficiente é Y 
    """
    n = len(points)
    diff_table = [[0 for _ in range(n)] for _ in range(n)] #cria uma matriz de zeros
    for i in range(n):
        diff_table[i][0] = points[i][1] # insere os valores de y na primeira coluna
        
    for j in range(1, n): #começa a partir da segunda coluna
        for i in range(n - j): #começa a partir da segunda linha
            diff_table[i][j] = (diff_table[i + 1][j - 1] - diff_table[i][j - 1]) / (points[i + j][0] - points[i][0]) #calcula a diferença dividida
    print([diff_table[0][i] for i in range(n)],"teste")
    print(diff_table)
    return [diff_table[0][i] for i in range(n)] #retorna a primeira linha da matriz
    
def newton_interpolation(x,points,coeficients):
    n = len(points)
    result = coeficients[0] #coeficiente inicial
    for i in range(1,n):
        term = coeficients[i] #coeficiente atual
        for j in range(i): #constroi o produto dos termos (x-x0)(x-x1)...(x-xj-1)
            term *= (x - points[j][0]) #faz a multiplicação dos termos (x-x0).(x-x1)...(x-xj-1)
        result += term
    return result