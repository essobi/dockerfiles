FROM ubuntu:12.04  
MAINTAINER Arcus "http://arcus.io"  
RUN echo "deb http://archive.ubuntu.com/ubuntu lucid main universe multiverse"
> /etc/apt/sources.list  
RUN apt-get update  
RUN apt-get install -y wget  
RUN wget http://www.rabbitmq.com/releases/rabbitmq-server/v3.1.5/rabbitmq-
server_3.1.5-1_all.deb -O /tmp/pkg.deb  
RUN RUNLEVEL=1 DEBIAN_FRONTEND=noninteractive dpkg -i /tmp/pkg.deb ; exit 0  
RUN RUNLEVEL=1 DEBIAN_FRONTEND=noninteractive apt-get -f -y install  
RUN rabbitmq-plugins enable rabbitmq_management  
  
ADD run.sh /usr/local/bin/run  
RUN chmod +x /usr/local/bin/run  
  
EXPOSE 5672  
EXPOSE 15672  
CMD ["/usr/local/bin/run"]  

