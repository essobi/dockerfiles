FROM jupyter/datascience-notebook  
  
MAINTAINER @joshuacook  
  
USER root  
  
RUN pip install mongoengine jupyterlab  
  
RUN jupyter serverextension enable \--py jupyterlab  
  
USER jovyan  

