FROM phusion/baseimage:latest  
  
RUN apt-get -y update  
RUN apt-get -y install git  
RUN apt-get -y install sudo wget  
RUN apt-get -y install sudo unzip  
RUN apt-get -y install sudo openjdk-7-jdk  
RUN cd /usr/local && wget
http://downloads.typesafe.com/play/2.2.3/play-2.2.3.zip && unzip
play-2.2.3.zip  
RUN cd /usr/local/src/ && git clone https://github.com/shimamoto/play2-hands-
on.git  
  
RUN /usr/sbin/enable_insecure_key  
  
EXPOSE 9000  
env PATH $PATH:/usr/local/play-2.2.3  
RUN cd /usr/local/src/play2-hands-on/play2-hands-on && play run  

