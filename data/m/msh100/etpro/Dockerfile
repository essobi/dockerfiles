FROM ubuntu:14.04  
MAINTAINER Marcus Hughes <hello@msh100.uk>  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update  
RUN apt-get -y upgrade  
RUN apt-get install -y ssh-client libc6-i386 wget php5-cli  
RUN echo 'variables_order = "EGPCS"' >> /etc/php5/cli/php.ini  
  
RUN useradd -ms /bin/bash game  
USER game  
WORKDIR /home/game  
  
RUN wget http://msh100.uk/files/et.tar  
RUN tar -xvf et.tar  
RUN rm -rf et.tar  
ADD start /home/game/  
  
RUN wget http://msh100.uk/files/libnoquery.so  
  
EXPOSE 27960/UDP  
  
CMD php start  

