FROM debian:8  
RUN echo "Europe/Berlin" > /etc/timezone && dpkg-reconfigure -f noninteractive
tzdata  
RUN apt-get update  
RUN apt-get install -y curl git apt-transport-https zip  
  
#Install NodeJS  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -  
RUN apt-get install -y nodejs  

