FROM ubuntu:14.04  
MAINTAINER Artur Taranchiev <ewok@ewok.ru>  
  
RUN apt-get update  
RUN apt-get install ziproxy pwgen -y  
  
RUN sed 's/# AuthMode = 0/AuthMode = 1/' -i /etc/ziproxy/ziproxy.conf  
RUN sed 's/# AuthPasswdFile/AuthPasswdFile/' -i /etc/ziproxy/ziproxy.conf  
  
# entrypoint  
WORKDIR /  
ADD run.sh /  
RUN chmod +x /run.sh  
  
ENTRYPOINT exec /run.sh  

