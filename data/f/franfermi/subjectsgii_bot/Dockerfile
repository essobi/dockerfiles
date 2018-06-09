FROM ubuntu:17.10  
MAINTAINER Francisco Fernández Millán <franfermi@correo.ugr.es>  
  
ARG DATABASE_URL  
ARG HOST_BD  
ARG NAME_BD  
ARG PW_BD  
ARG USER_BD  
ARG TOKEN  
  
ENV DATABASE_URL=$DATABASE_URL  
ENV HOST_BD=$HOST_BD  
ENV NAME_BD=$NAME_BD  
ENV PW_BD=$PW_BD  
ENV USER_BD=$USER_BD  
ENV TOKEN=$TOKEN  
  
RUN apt-get update  
RUN apt-get install -y python3-pip  
RUN apt-get install -y git  
RUN git clone https://github.com/franfermi/Infraestructura-Virtual_IV.git  
RUN cd Infraestructura-Virtual_IV/ && pip3 install -r requirements.txt  
  
EXPOSE 8000  
WORKDIR Infraestructura-Virtual_IV/  
CMD gunicorn API_web:app --log-file=- --bind 0.0.0.0:8000  

