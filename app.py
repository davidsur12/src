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
        print('NCP',str(NCP))
        print('Type de ncp', type(NCP))
        print('Transporte ' , str(MTRANS))
        datos = [float(gender), normalizarVariable2(age, 0 , 100),  normalizarVariable2(height, 1.2 ,2 ), normalizarVariable2(weight, 40 , 170),
                 float(antecedentes), float(FAVC),  normalizarVariable(FCVC, 0 , 2),  normalizarVariable(NCP, 0 , 3),
                 normalizarVariable(CAEC, 0 , 3), float(SMOKE), normalizarVariable(CH2O, 0 , 2) ,
                 float(SCC), normalizarVariable(FAF, 0 , 3), normalizarVariable(TUE, 0 , 2),
                 normalizarVariable(CALC , 0 , 3) ,normalizarVariable(MTRANS , 0 , 3)]
        
        datos2 = [float(gender), normalizarVariable(age, 0 , 100),  
                 float(antecedentes), float(FAVC),  normalizarVariable(FCVC, 1 , 3),  normalizarVariable(NCP, 1 , 4),
                 normalizarVariable(CAEC, 1 , 4), float(SMOKE), normalizarVariable(CH2O, 1 , 3) ,
                 float(SCC), normalizarVariable(FAF, 1 , 4), normalizarVariable(TUE, 1 , 3),
                 normalizarVariable(CALC , 1 , 4) ,normalizarVariable(MTRANS , 0 , 3)]
        datos3 = [1,	0.2765957,	0.66038,	0.358209,	0,	0,	1,	0.666667,	0.666667,	0,	0.5,	0,	0.666667,	0,	0.333333,	1]
        
        rr = (calcular_imc(float(weight), float(height))) #en kilogramos
    
        
         
        print('Dtaos normalizados de la tabla 2')
        
        for n in datos:
            print('date normalisados ', n)
            #print(n)
        print('date  recibido')
        m=ModeloOrange()
        r=m.informe(datos) 
        
        #return ('el rsultado fue'  + str(r) + 'IMC ' + str(rr) )  
        imc= calcular_obesidad(float(weight), float(height))
        data = {'title':'Result', 'imc': rr,  'result': tipoObesidad(r), 'imcpeso': imc, 'result2':tipoObesidad2(r)}
        
        return render_template('resultado.html', data=data)
 
def categorizar_imc(imc):
    
    if imc < 18.5:
        return "Bajo peso"
    elif 18.5 <= imc < 25:
        return "Peso normal"
    elif 25 <= imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidad"
       
def calcular_obesidad(peso, altura):
    # Calcula el IMC
    imc = peso / (altura ** 2)
    return imc
    
def normalizarVariable(variable, num_min, num_max):
    return float(((float(variable)-1.0) - num_min)/(num_max-num_min))

def normalizarVariable2(variable, num_min, num_max):
    return float(((float(variable)) - num_min)/(num_max-num_min))

def tipoObesidad(id):
    id=id+1
    if(id == 1):
        return 'peso insuficiente'
    if(id == 2):
        return 'peso normal'
    if(id == 3):
        return 'sobrepeso nivel I'
    if(id == 4):
        return 'sobrepeso nivel II'
    if(id == 5):
        return 'obesidad tipo I'
    if(id == 6):
        return 'obesidad tipo 2'
    if(id == 7):
        return 'obesidad tipo 3'
    else:
        return ('obesidad tipo 3')
      
def tipoObesidad2(id):
    id=id+1
    if(id == 1):
        return ['Recuerda que el impacto del peso insuficiente en el aprendizaje puede ser significativo. Aquí hay algunas formas en que podría afectar:'
            'La malnutrición puede afectar negativamente las habilidades cognitivas, como el razonamiento, la resolución de problemas y la toma de decisiones.',
                'En el caso de niños y adolescentes, la malnutrición puede afectar el desarrollo físico y mental, lo que podría tener repercusiones a largo plazo en su capacidad de aprendizaje y logro académico.',
                'La falta de nutrientes adecuados puede afectar la función cerebral, incluida la memoria. Una dieta deficiente puede hacer que sea más difícil recordar información y retenerla a largo plazo.']
    if(id == 2):
        return ['Mantener un peso normal es fundamental para la salud y el bienestar en general. Aquí hay algunas razones importantes para mantener un peso adecuado:',
                'Salud física: Un peso normal está asociado con un menor riesgo de desarrollar una variedad de problemas de salud.',
                'Salud mental: El peso corporal también puede afectar la salud mental y emocional.',
                'Calidad de vida: Un peso saludable puede mejorar significativamente la calidad de vida.',
                'Longevidad: Estudios han demostrado que mantener un peso normal está asociado con una mayor esperanza de vida.',
                'Prevención de enfermedades: Mantener un peso normal puede ayudar a prevenir una serie de enfermedades crónicas.']
    if(id == 3):
        return ['El impacto del sobrepeso de nivel I en el aprendizaje puede ser notable. Aquí hay algunas formas en que podría afectar:',
                'Autoestima y confianza',
                'Fatiga y falta de energía',
                'Problemas de salud']
    if(id == 4):
        return ['El sobrepeso de nivel II, también conocido como obesidad, puede tener un impacto aún más significativo en el aprendizaje. Aquí hay algunas formas en que podría afectar:',
                "Problemas de salud física",
    "Fatiga y falta de energía",
    "Problemas de autoestima y ansiedad",
    "Dificultades sociales",
    "Problemas de atención y concentración",
    "Participación en actividades físicas"]
    if(id == 5):
        return ['La obesidad de tipo I, también conocida como obesidad mórbida o severa, puede tener un impacto significativo en el aprendizaje. Aquí están algunos de los efectos que podría tener:',
                'Problemas de salud física graves: La obesidad de tipo I está asociada con un mayor riesgo de desarrollar enfermedades crónicas graves, como enfermedades cardíacas, diabetes tipo 2, apnea del sueño, enfermedades articulares y problemas respiratorios. Estas condiciones de salud pueden afectar negativamente la energía, la concentración y la capacidad de aprendizaje en el aula.',
                'Fatiga y falta de energía crónicas: Las personas con obesidad mórbida a menudo experimentan fatiga crónica y falta de energía debido al esfuerzo adicional que su cuerpo requiere para realizar actividades diarias. Esta fatiga puede dificultar la concentración y el rendimiento académico.',
                'Problemas de movilidad: La obesidad severa puede dificultar la movilidad y la comodidad física, lo que puede afectar la participación en actividades escolares, como deportes o actividades físicas, así como la interacción social con otros estudiantes.',
                'Necesidades educativas especiales: Algunos niños con obesidad de tipo I pueden necesitar apoyo adicional en el aula, como ajustes en la silla o escritorio para mayor comodidad, acceso a alimentos saludables en la escuela y programas de educación física adaptados para satisfacer sus necesidades específicas.']
    if(id == 6):
         return ['La obesidad de tipo II, también conocida como obesidad mórbida o severa, puede tener un impacto significativo en el aprendizaje. Aquí están algunos de los efectos que podría tener:',
                'Problemas de salud física graves: La obesidad de tipo I está asociada con un mayor riesgo de desarrollar enfermedades crónicas graves, como enfermedades cardíacas, diabetes tipo 2, apnea del sueño, enfermedades articulares y problemas respiratorios. Estas condiciones de salud pueden afectar negativamente la energía, la concentración y la capacidad de aprendizaje en el aula.',
                'Fatiga y falta de energía crónicas: Las personas con obesidad mórbida a menudo experimentan fatiga crónica y falta de energía debido al esfuerzo adicional que su cuerpo requiere para realizar actividades diarias. Esta fatiga puede dificultar la concentración y el rendimiento académico.',
                'Problemas de movilidad: La obesidad severa puede dificultar la movilidad y la comodidad física, lo que puede afectar la participación en actividades escolares, como deportes o actividades físicas, así como la interacción social con otros estudiantes.',
                'Necesidades educativas especiales: Algunos niños con obesidad de tipo I pueden necesitar apoyo adicional en el aula, como ajustes en la silla o escritorio para mayor comodidad, acceso a alimentos saludables en la escuela y programas de educación física adaptados para satisfacer sus necesidades específicas.']
    if(id == 7):
        return ['La obesidad de tipo III, también conocida como obesidad mórbida o severa, puede tener un impacto significativo en el aprendizaje. Aquí están algunos de los efectos que podría tener:',
                'Problemas de salud física graves: La obesidad de tipo I está asociada con un mayor riesgo de desarrollar enfermedades crónicas graves, como enfermedades cardíacas, diabetes tipo 2, apnea del sueño, enfermedades articulares y problemas respiratorios. Estas condiciones de salud pueden afectar negativamente la energía, la concentración y la capacidad de aprendizaje en el aula.',
                'Fatiga y falta de energía crónicas: Las personas con obesidad mórbida a menudo experimentan fatiga crónica y falta de energía debido al esfuerzo adicional que su cuerpo requiere para realizar actividades diarias. Esta fatiga puede dificultar la concentración y el rendimiento académico.',
                'Problemas de movilidad: La obesidad severa puede dificultar la movilidad y la comodidad física, lo que puede afectar la participación en actividades escolares, como deportes o actividades físicas, así como la interacción social con otros estudiantes.',
                'Necesidades educativas especiales: Algunos niños con obesidad de tipo I pueden necesitar apoyo adicional en el aula, como ajustes en la silla o escritorio para mayor comodidad, acceso a alimentos saludables en la escuela y programas de educación física adaptados para satisfacer sus necesidades específicas.']
        
    else:
        return ('obesidad tipo 3')
            
def calcular_imc(peso, altura):
    """
    Calcula el Índice de Masa Corporal (IMC) dado el peso (en kg) y la altura (en metros).
    Devuelve la categoría de peso correspondiente.
    """
    imc = peso / (altura ** 2)
    
    if imc < 18.5:
        return "Peso insuficiente"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 24.9 <= imc < 29.9:
        return "Sobrepeso nivel I"
    elif 29.9 <= imc < 34.9:
        return "Sobrepeso nivel II"
    elif 34.9 <= imc < 39.9:
        return "Obesidad tipo I"
    elif 39.9 <= imc < 49.9:
        return "Obesidad tipo II"
    else:
        return "Obesidad tipo III"       
     

       
if __name__ == '__main__':
    app.config.from_object(config['developmet'])
    app.run()