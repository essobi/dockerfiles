FROM jupyter/tensorflow-notebook  
  
  
  
ADD . /question_rec  
WORKDIR /question_rec  
#RUN pip install -r requirements.txt  
# Install apt-get stuff  
USER root  
RUN sudo apt-get update  
EXPOSE 8888  
  
USER $NB_USER  
CMD ["jupyter", "notebook", "--port=8888", "--no-browser", "--ip=0.0.0.0", "--
allow-root"]

