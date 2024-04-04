from flask import Flask, render_template,  request
from config import config
from modelo import ModeloOrange

app = Flask(__name__)


@app.route('/')
def index():
    data ={'title': 'Formulario'}
    #m=ModeloOrange()
    #m.informe()
    return render_template('formulario.html', data=data)
    #return 'hi' 
    
@app.route('/procesar', methods=['POST'])
def submit():
    if request.method == 'POST':
        gender = request.form['gender']
        age = request.form['age']
        height = request.form['height']
        weight = request.form['weight']
        antecedentes = request.form['antecedentes']
        FAVC = request.form['FAVC']
        FCVC = request.form['FCVC']
        NCP = request.form['NCP']
        CAEC = request.form['CAEC']
        SMOKE = request.form['SMOKE']
        CH2O = request.form['CH2O']
        SCC = request.form['SCC']
        FAF = request.form['FAF']
        TUE = request.form['TUE']
        CALC = request.form['CALC']
        MTRANS = request.form['MTRANS']
   
        print(gender , 'genero')
        print('age ', age)
        print('height' , height)
        print('weight', weight)
        print('antecedentes ', str(antecedentes))
        print('FAVC', str(FAVC))
        print('FCVC', str(FCVC))
        
        datos = [float(gender), normalizarVariable(age, 0 , 100),  normalizarVariable(height, 0 , 100), normalizarVariable(weight, 0 , 100),
                 float(antecedentes), float(FAVC),  normalizarVariable(FCVC, 1 , 3),  normalizarVariable(NCP, 1 , 4),
                 normalizarVariable(CAEC, 1 , 4), float(SMOKE), normalizarVariable(CH2O, 1 , 3) ,
                 float(SCC), normalizarVariable(FAF, 1 , 4), normalizarVariable(TUE, 1 , 3),
                 normalizarVariable(CALC , 1 , 4) ,normalizarVariable(MTRANS , 1 , 4)]
        
        obeso = calcular_obesidad(float(weight), float(height))#en kilogramos
        rr=''
        if(obeso == 1):
           rr='Eres obeso'
        else:
           rr='No eres obeso'   
        
        for n in datos:
            print( n)
            #print(n)
        print('date  recibido')
        m=ModeloOrange()
        r=m.informe(datos) 
        
        #return ('el rsultado fue'  + str(r) + 'IMC ' + str(rr) )  
        data = {'title':'Result', 'imc': rr,  'result': tipoObesidad(r)}
        return render_template('resultado.html', data=data)
 
   
def calcular_obesidad(peso, altura):
    # Calcula el IMC
    imc = peso / (altura ** 2)
    
    # Determina si hay obesidad
    if imc >= 30:
        return 1
    else:
        return 0
    
def normalizarVariable(variable, num_min, num_max):
    return float((float(variable) - num_min)/(num_max-num_min))
    


def tipoObesidad(id):
    if(id == 0):
        return 'peso insuficiente'
    if(id == 1):
        return 'peso normal'
    if(id == 2):
        return 'sobrepeso nivel I'
    if(id == 3):
        return 'sobrepeso nivel II'
    if(id == 4):
        return 'obesidad tipo I'
    if(id == 5):
        return 'obesidad tipo 2'
    if(id == 6):
        return 'obesidad tipo 3'
        
    
        
     

       
if __name__ == '__main__':
    app.config.from_object(config['developmet'])
    app.run()