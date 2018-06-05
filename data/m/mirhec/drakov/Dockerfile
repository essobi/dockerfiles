FROM spira/docker-npm  
  
MAINTAINER "Zak Henry" <zak.henry@gmail.com>  
  
WORKDIR /tmp  
  
RUN npm install -g drakov  
  
# Drakov startup script  
ADD config/drakov-start.sh /opt/bin/drakov-start.sh  
RUN chmod u=rwx /opt/bin/drakov-start.sh  
  
RUN mkdir -p /data  
  
# PORTS  
EXPOSE 3000  
WORKDIR /opt/bin  
ENTRYPOINT ["/opt/bin/drakov-start.sh"]  

