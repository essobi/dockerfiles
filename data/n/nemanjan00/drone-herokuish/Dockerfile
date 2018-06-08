FROM ubuntu:14.04  
USER root  
  
# install docker  
RUN apt-get install -y apparmor curl  
RUN curl -s https://get.docker.io/ubuntu/ | sudo sh  
ADD deps/jpetazzo/dind/wrapdocker /usr/local/bin/wrapdocker  
RUN chmod +x /usr/local/bin/wrapdocker  
  

