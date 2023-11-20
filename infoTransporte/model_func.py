import numpy as np
from sklearn.preprocessing import StandardScaler
import joblib

def prediction(traffic,weather,accident,rush_hour,day_month,distance,festive,dayofweek):
    scaler = StandardScaler()
    # Load the saved model
    loaded_model = joblib.load('modelo_prediccion/xgboost_model.joblib')
    # Define the input parameters for prediction
    #features = ['nivel_trafico', 'clima', 'accidente', 'es_hora_punta', 'dia_del_ano', 'distancia', 'es_festivo', 'dia_semana']
    sample_input_params = np.array([[1, 0, 0,False,100,200,False,3]])
    # Scale the input parameters if needed (use the same scaler you used for training)
    scaled_sample_input_params = scaler.transform(sample_input_params)
    # Make a prediction
    prediction = loaded_model.predict(scaled_sample_input_params)
    return prediction[0]