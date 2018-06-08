# dockerized (minimal: <1GB) jupyter notebook for pythonic data science  
FROM jupyter/notebook  
  
MAINTAINER Enrique Otero <enrique.otero@beeva.com>  
  
RUN apt-get update && apt-get install -y libfreetype6-dev libatlas-base-dev
gfortran  
RUN pip2 install pandas matplotlib scipy scikit-learn  

