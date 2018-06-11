FROM alpine  
  
RUN apk update && \  
apk add --no-cache py-pip  
  
RUN pip install shadowsocks  
  
COPY start.sh /opt/start.sh  
RUN chmod +x /opt/start.sh  
  
CMD ["/opt/start.sh"]  

