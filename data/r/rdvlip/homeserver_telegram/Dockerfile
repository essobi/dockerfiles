FROM rdvlip/base  
  
MAINTAINER Dmitry Romanov <rdvlip@gmail.com>  
  
LABEL "repo" "rdvlip/homeserver_telegram"  
  
ADD . /code/  
WORKDIR /code  
  
RUN pip3 install -r requirements.txt  
  
CMD python3 main.py

