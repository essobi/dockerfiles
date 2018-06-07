FROM continuumio/anaconda:4.2.0  
  
RUN pip install grpcio-tools networkx  
  
ADD ./service /app  
  
CMD ["python","/app/service.py"]  

