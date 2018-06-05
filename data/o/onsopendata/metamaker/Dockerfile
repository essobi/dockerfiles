FROM ubuntu:14.04  
RUN apt-get -y update  
RUN apt-get -y upgrade  
RUN apt-get install -y software-properties-common  
RUN add-apt-repository ppa:fkrull/deadsnakes-python2.7  
RUN apt-get -y update  
RUN apt-get -y upgrade  
  
RUN apt-get install -y git python-pip python-dev libffi-dev libssl-dev build-
essential  
RUN pip install --upgrade pip  
RUN pip install --upgrade ndg-httpsclient  
RUN pip install 'requests[security]'  
  
RUN pip install django  
RUN pip install django_jinja  
RUN pip install djangorestframework  
  
RUN git clone https://github.com/ONS-OpenData/MetaMaker  
  
CMD python ./MetaMaker/metamaker_django/manage.py runserver 0.0.0.0:8000  

