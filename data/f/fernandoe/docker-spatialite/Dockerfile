FROM fernandoe/docker-python:0.0.4  
MAINTAINER Fernando Espíndola <fer.esp@gmail.com>  
  
RUN apt-get update && apt-get upgrade -y  
  
RUN apt-get -y install python-dev  
RUN apt-get -y install libpq-dev  
RUN apt-get -y install python-lxml  
  
RUN apt-get -y install libxml2-dev  
RUN apt-get -y install libxslt1-dev  
RUN apt-get -y install zlib1g-dev  
  
RUN apt-get -y install binutils libproj-dev gdal-bin  
RUN apt-get -y install libcairo2-dev  
RUN apt-get -y install pango1.0-tests  
  
RUN apt-get -y autoremove  
RUN apt-get -y autoclean  
RUN apt-get -y clean  
  
RUN pip install pip setuptools -U  
RUN pip install amqp  
RUN pip install anyjson  
  
ADD requirements.txt /requirements.txt  
RUN pip install -r /requirements.txt  

