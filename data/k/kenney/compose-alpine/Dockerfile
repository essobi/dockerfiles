FROM docker:latest  
MAINTAINER Kenney He<kenneyhe@gmail.com>  
RUN apk update  
RUN apk upgrade  
RUN apk add py-pip  
RUN pip install docker-compose  
ADD autostart.sh /  
RUN chmod u+x /autostart.sh  
ENTRYPOINT ./autostart.sh  

