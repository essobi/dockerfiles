FROM ubuntu  
MAINTAINER oxoox22@gmail.com <Oxoox Soulmaneller>  
  
RUN apt-get update  
RUN apt-get -y upgrade  
RUN apt-get -y autoremove  
RUN apt-get -y dist-upgrade  
RUN apt-get install -y openssh-server openssh-client  
RUN apt-get install -y wget curl  
RUN apt-get install -y expect rsync  
  
WORKDIR /root  
CMD [ "bash" ]  

