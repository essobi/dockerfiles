FROM python:3  
MAINTAINER Ramón Gago Carrera <ramongagocarrera@gmail.com>  
  
WORKDIR /usr/src/app  
  
# Instala python-pip  
RUN pip install --no-cache-dir  
  
# Instala flask y las librerías necesarias  
RUN pip install flask flask-restful flask-jsonpify pymongo  
  
COPY contenedores/server.py /app  
  
ENTRYPOINT ["python"]  

