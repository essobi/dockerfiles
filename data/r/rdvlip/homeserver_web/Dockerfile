FROM rdvlip/base  
  
MAINTAINER Dmitriy Romanov <rdvlip@gmail.com>  
  
LABEL "repo" "rdvlip/homeserver_web"  
  
ADD . /code/  
WORKDIR /code  
  
RUN pip3 install -r requirements.txt  
  
CMD python3 main.py

