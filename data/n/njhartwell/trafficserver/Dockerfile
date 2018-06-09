FROM debian:wheezy  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get -q update && apt-get install -y trafficserver && rm -r
/var/lib/apt/lists/*  
RUN mkdir /var/run/trafficserver && chown trafficserver:trafficserver
/var/run/trafficserver  
  
EXPOSE 8080  
CMD ["traffic_manager"]  

