FROM tensorflow/tensorflow:1.4.0  
RUN apt-get update  
  
RUN pip install flask  
RUN apt-get install -y git  
RUN git clone https://github.com/lastlegion/predict_api.git  
WORKDIR /notebooks/predict_api  
CMD ["python", "server.py"]  
  

