FROM python:3  
WORKDIR /opt  
  
RUN pip install flask requests wasp-eureka python-jose flask_cors pyowm
pymongo pytest scipy numpy pandas statsmodels  
  
COPY GlucosaChi.py /opt/  
COPY Controller_ClucosaChi.py /opt/  
COPY Bi_glucose_swagger.json /opt/  
COPY register.py /opt/  
COPY runAll.py /opt/  
COPY Controller_Routes.py /opt/  
COPY UrlParse.py /opt/  
COPY forecast.py /opt/  
COPY forecast_datetime.json /opt/  
COPY multipoligono.json /opt/  
COPY modelsController.py /opt/  
  
EXPOSE 7000  
CMD python3 ./runAll.py  

