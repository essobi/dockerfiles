FROM ubuntu:14.04  
MAINTAINER Will Refvem <will.refvem@raleighnc.gov>  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
RUN apt-get update && apt-get install -y python python-dev python-setuptools
git  
RUN easy_install pip  
RUN git clone https://github.com/wbrefvem/corkboard.git  
RUN cd /corkboard && pip install -r requirements.txt  
WORKDIR /corkboard/corkboard  
RUN touch corkboard/secrets.py && printf "RABBITMQ_USER = ''\nRABBITMQ_PWD =
''" >> corkboard/secrets.py  
RUN python manage.py migrate  

