FROM ubuntu:16.04  
MAINTAINER Jose Gomez Baena  
  
# Variables de entorno para la conexion a la BD y para el Bot  
ARG DATABASE_URL  
ARG token_bot  
  
ENV DATABASE_URL=$DATABASE_URL  
ENV token_bot=$token_bot  
  
  
RUN apt-get update  
RUN apt-get install -y python3-pip  
RUN apt-get install -y git  
RUN git clone https://github.com/josegob/IV-Proyecto.git  
RUN cd IV-Proyecto/ && pip3 install -r requirements.txt  
EXPOSE 80  
WORKDIR IV-Proyecto/  
  
CMD ["gunicorn", "--config=config_gunicorn.py", "flask_api:app"]  

