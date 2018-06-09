FROM debian:stable  
MAINTAINER Thomas Kerpe <thomas@kerpe.net>  
  
RUN apt-get update && apt-get install -y git build-essential  
RUN mkdir /tmp/src  
RUN cd /tmp/src ; git clone
git://git.eclipse.org/gitroot/mosquitto/org.eclipse.mosquitto.rsmb.git  
RUN cd /tmp/src/org.eclipse.mosquitto.rsmb/rsmb/src ; make && cp broker*
Messages.1.3.0.2 /usr/local/bin/  
  
VOLUME ["/mqtt/config"]  
COPY config/rsmb.conf /mqtt/config/  
  
EXPOSE 1883  
EXPOSE 1885/udp  
  
CMD ["broker_mqtts", "/mqtt/config/rsmb.conf"]  

