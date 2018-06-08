FROM jupyter/all-spark-notebook  
  
MAINTAINER Paul Gesiak  
  
  
USER jovyan  
# # copy demo repository to user's folder  
# RUN git clone https://github.com/hibariba/jupyter-demo.git
/home/jovyan/work/jupyter-demo  
COPY notebooks /home/jovyan/work  
  
# switch back to root  
# (otherwise jupyter service would not start)  
USER root  
  
# allow attaching external volume here:  
VOLUME /data  

