FROM python:3.5  
RUN git clone https://github.com/grpc/grpc && \  
mv grpc/examples/python/helloworld /opt/ && \  
rm -rf grpc  
  
RUN pip install grpcio==1.0.0rc2  
  
EXPOSE 50051  
ENTRYPOINT ["python3.5", "/opt/helloworld/greeter_server.py"]  

