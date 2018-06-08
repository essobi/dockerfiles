FROM python:2.7  
MAINTAINER Ranger.Huang <killua.vx@gmail.com>  
ENV REFRESH_AT 2016-09-03  
RUN mkdir /code  
WORKDIR /code  
COPY ./zbar.sh .  
RUN sh zbar.sh  
  
COPY ./requirements.txt .  
RUN pip install -r requirements.txt  
  
COPY ./reconfig.py .  
  
COPY ./config.yaml .  
ENV CONFIG_FILE='./config.yaml'  
CMD ""  
ENTRYPOINT /usr/local/bin/python reconfig.py "$CONFIG_FILE"  

