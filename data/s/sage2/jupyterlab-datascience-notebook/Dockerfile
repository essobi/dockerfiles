FROM jupyter/datascience-notebook  
  
MAINTAINER Andrew Burks <andrewtburks@gmail.com>  
  
USER root  
COPY . jupyterlab_sage2/  
  
RUN jupyter labextension install ./jupyterlab_sage2/  
RUN rm -rf ./jupyterlab_sage2  
USER $NB_USER

