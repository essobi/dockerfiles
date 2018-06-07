FROM debian:jessie  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && \  
apt-get install -y wget apt-utils  
RUN wget http://repo.mosquitto.org/debian/mosquitto-repo.gpg.key | bash && \  
apt-key add mosquitto-repo.gpg.key  
RUN cd /etc/apt/sources.list.d && \  
wget http://repo.mosquitto.org/debian/mosquitto-jessie.list | bash  
  
RUN apt-get update && \  
apt-get install -y mosquitto mosquitto-clients  
  
RUN cd /etc/mosquitto && \  
echo "listener 1883 0.0.0.0" >> mosquitto.conf && \  
echo "protocol mqtt" >> mosquitto.conf && \  
echo "listener 8080 0.0.0.0" >> mosquitto.conf && \  
echo "protocol websockets" >> mosquitto.conf  
  
RUN cd /etc/mosquitto/conf.d  
ADD mosquitto.conf /etc/mosquitto/conf.d/mosquitto.conf  
RUN cd /etc/mosquitto && \  
mkdir password && \  
chown 777 -R /etc/mosquitto/password  
RUN service mosquitto restart && \  
service mosquitto stop  
  
ADD run.sh /etc/mosquitto/run.sh  
RUN cd /etc/mosquitto/ && \  
chmod +x run.sh  
  
VOLUME /etc/mosquitto/password/  
  
EXPOSE 8080 1883  
CMD /etc/mosquitto/run.sh  
  

