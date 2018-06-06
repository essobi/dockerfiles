FROM jupyter/all-spark-notebook  
  
MAINTAINER @joshuacook  
  
USER root  
  
ENV TF_BINARY_URL
https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-0.9.0-cp35-cp35m-linux_x86_64.whl  
  
RUN curl https://bootstrap.pypa.io/ez_setup.py -o - | python  
  
RUN pip3 install --upgrade $TF_BINARY_URL  
RUN pip3 install mongoengine  
  
USER jovyan  

