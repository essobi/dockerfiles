FROM debian  
  
RUN apt-get update && apt-get install -y tinc vim tar less ifupdown net-tools
curl unzip  
  
# template files copy  
COPY config /etc/tinc-templates  
  
COPY files/start.sh /opt/start.sh  
RUN chmod +x /opt/start.sh  
  
VOLUME /etc/tinc  
  
ENTRYPOINT /opt/start.sh  

