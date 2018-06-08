FROM dock0/service  
MAINTAINER Jon Chen <bsd@voltaire.sh>  
  
RUN pacman -Syu --noconfirm --needed python python-pip  
  
ADD ./config.json /etc/pugbot_ng.json  
  
RUN /usr/bin/pip3 install pugbot_ng  
  
ADD run /service/pugbotng/run  

