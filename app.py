from flask import Flask, render_template,  request
from config import config

app = Flask(__name__)


@app.route('/')
def index():
    data ={'title': 'Formulario'}
    return render_template('formulario.html', data=data)
    #return 'hi' 
    
@app.route('/submit', methods=['POST'])
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
        datos = [gender, age, height, weight, antecedentes, FAVC, FCVC, NCP, CAEC, SMOKE, CH2O, SCC, FAF, TUE ,CALC ,MTRANS]
       
        
        for n in datos:
            print(str(n))
        print('date  recibido')
        
        return 'Formulario enviado exitosamente'   
    
 
if __name__ == '__main__':
    app.config.from_object(config['developmet'])
    app.run()