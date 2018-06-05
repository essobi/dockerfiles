FROM debian:wheezy  
  
MAINTAINER Romain Fihue <romain.fihue@gmail.com>  
  
RUN apt-get update > /dev/null  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -q -y wget openjdk-7-jdk  
  
RUN wget -O /tmp/go-server.deb http://download.go.cd/gocd-deb/go-
server-14.4.0-1356.deb  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -q -y unzip git  
  
RUN dpkg -i /tmp/go-server.deb  
  
RUN ln -s /dev/stdout /var/log/go-server/go-server.log  
  
ADD go-server /etc/default/go-server  
  
EXPOSE 8153  
#CMD /bin/su - go -c /usr/share/go-server/server.sh  
CMD /usr/share/go-server/server.sh  
  

