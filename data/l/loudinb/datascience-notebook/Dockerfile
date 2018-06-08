FROM jupyter/datascience-notebook  
  
USER root  
  
RUN apt-get -y update && apt-get -y upgrade && apt-get install -y
libsasl2-modules libsasl2-dev  
  
USER jovyan  
  
ADD requirements.txt .  
RUN pip install -r requirements.txt  

