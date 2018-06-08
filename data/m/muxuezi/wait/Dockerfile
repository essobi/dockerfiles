FROM ubuntu:14.04  
RUN apt-get update  
RUN apt-get install -y python-setuptools libevent-dev gcc python-dev  
RUN easy_install pip  
RUN pip install virtualenv  
ENV VENV_DIR /code/venv  
RUN virtualenv $VENV_DIR  
RUN $VENV_DIR/bin/pip install flask-sockets gunicorn  
RUN echo "source $VENV_DIR/bin/activate" >> ~/.bashrc  
  
# fichier d'exemple hello.py (override-able)  
ADD hello.py /code/work/hello.py  
  
# volumes  
VOLUME /code/work  
  
# on change de répertoire de travail  
WORKDIR /code/work  
  
# on rend le port accessible à la machine hôte  
EXPOSE 8000  
# on définit la commande par défaut  
ENTRYPOINT ["/bin/bash"]  
  

