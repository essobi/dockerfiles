# AYB: Intel Snap telemetry  
# AYB: Version 0.0.1  
#  
# 0.0.1: initial commit (snap v0.15.0_beta)  
FROM golang:latest  
  
  
MAINTAINER Ayoub Boulila <ayoubboulila@gmail.com>  
  
ENV GOPATH=$GOPATH:/app SNAP_PATH=/opt/snap \  
TRUST=0 TRIBEPORT=6001 APIPORT=8181 SEEDIP=127.0.0.1 SEEDPORT=6000
TRIBEADDR=127.0.0.1  
  
WORKDIR /home  
ADD resources/bin.zip /home/resources/bin.zip  
ADD resources/plugin1.zip /home/resources/plugin1.zip  
ADD resources/plugin2.zip /home/resources/plugin2.zip  
  
RUN apt-get update && apt-get install unzip && apt-get clean autoclean && apt-
get autoremove && unzip /home/resources/bin.zip -d /opt && \  
unzip -o /home/resources/plugin1.zip -d /home/resources/ && \  
unzip -o /home/resources/plugin2.zip -d /home/resources/ && \  
mv /home/resources/plugin/snap-plugin-collector-docker /opt/snap/plugin/ && \  
mv /home/resources/plugin/snap-plugin-publisher-influxdb /opt/snap/plugin/ &&
\  
rm /home/resources/bin.zip && \  
rm /home/resources/plugin1.zip && \  
rm /home/resources/plugin2.zip  
  
ADD ./startup.sh /opt/snap/startup.sh  
RUN chmod -R 777 /opt/snap/  
RUN chmod +x /opt/snap/startup.sh  
  
# Ports  
EXPOSE 8181 6000 6001  
  
  
ENV PATH=$PATH:/opt/snap/bin  
USER root  
# EXEC  
CMD ["run"]  
ENTRYPOINT ["/opt/snap/startup.sh"]  

