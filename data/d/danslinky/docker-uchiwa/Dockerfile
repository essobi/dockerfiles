FROM danslinky/docker-sensu  
  
RUN \  
apt-get update && \  
apt-get install -y uchiwa && \  
apt-get clean all  
  
EXPOSE 3000  
  
CMD ["/opt/uchiwa/bin/uchiwa", "-c", "/etc/sensu/uchiwa.json", "-p",
"/opt/uchiwa/src/public"]  

