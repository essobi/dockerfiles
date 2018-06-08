FROM golang:1.10.0  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash  
  
RUN apt-get update && \  
apt-get -y upgrade && \  
apt-get -y install nodejs && \  
apt-get clean  
  
CMD /bin/bash  

