FROM python:3-alpine  
MAINTAINER Michael Erasmus <hi@michaelerasm.us>  
  
RUN pip install moto[server]  
  
EXPOSE 5000  
ENTRYPOINT ["moto_server"]  

