FROM maxird/centos:7  
LABEL Name=dnsfw \  
Version=1.0.0  
  
EXPOSE 53/udp 53/tcp  
VOLUME /config  
  
ADD run /app/  
ADD reload /app/  
ADD rotate /app/  
ADD domains.conf /defaults/  
ADD local.conf /defaults/  
RUN mkdir -p /config && \  
chmod +x /app/*  
  
ENV PATH $PATH:/app  
WORKDIR /app  
  
CMD ["run"]  

