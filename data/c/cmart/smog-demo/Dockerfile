# This builds a docker image for smog: Simple Markdown blOG.  
# Right now it runs the debug server which is ONLY for testing/evaluation
purposes. It is INSECURE and should not be used for production.  
FROM debian  
MAINTAINER Chris Martin  
RUN apt-get update  
RUN apt-get install -y tar git curl vim wget  
RUN apt-get install -y python python-dev python-pip python-virtualenv  
RUN virtualenv smog-venv  
RUN . smog-venv/bin/activate  
RUN git clone https://github.com/c-mart/smog.git  
WORKDIR /smog  
RUN pip install -r requirements.txt  
EXPOSE 80  
CMD python manage.py init_db && python run_debug_server.py

