FROM debian:jessie  
ENV BROKER_HOST 127.0.0.1  
RUN echo "deb http://ftp.debian.org/debian jessie-backports main" >>
/etc/apt/sources.list  
RUN apt-get update  
RUN apt-get install wget -y  
RUN apt-get -t jessie-backports install openjdk-8-jre -y  
RUN wget
https://github.com/yahoo/pulsar/releases/download/v1.15.2/pulsar-1.15.2-bin.tar.gz  
RUN tar zxvf pulsar-1.15.2-bin.tar.gz  
ADD start_pulsar.sh /pulsar-1.15.2/  
EXPOSE 8080  
EXPOSE 6650  
WORKDIR /pulsar-1.15.2  
CMD ["/bin/sh", "./start_pulsar.sh"]  
  

