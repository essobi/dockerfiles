FROM tensorflow/tensorflow:latest  
  
WORKDIR /code  
COPY requirements.txt /code/  
RUN pip install -r requirements.txt  
  
COPY dataset /code/dataset  
COPY wideep /code/wideep  
COPY launch.sh setup.py /code/  
  
ENTRYPOINT ["python", "./wideep/net_mk1.py"]  

