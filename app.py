from flask import Falsk,request,render_template

from src.pipeline.predict_pipeline import CustomData,PredictPipeline

webapp = Falsk(__name__)

@webapp.route('/')
def index():
    return render_template('index.html')

@webapp.route('predict_data',methods=['GET','POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('prediction.html')

    if request.method == 'POST':
        


        return render_template('prediction.html')


