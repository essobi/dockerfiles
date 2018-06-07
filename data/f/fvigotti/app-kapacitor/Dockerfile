FROM debian:jessie  
  
ENV HOSTNAME localhost  
ENV INFLUXDB_URL http://localhost:8086  
ENV DEBIAN_FRONTEND noninteractive  
ENV KAPACITOR_VERSION 0.10.1-1  
RUN apt-get update && \  
apt-get install -y curl && \  
curl -O
https://s3.amazonaws.com/influxdb/kapacitor_${KAPACITOR_VERSION}_amd64.deb &&
\  
dpkg -i kapacitor_${KAPACITOR_VERSION}_amd64.deb && rm
kapacitor_${KAPACITOR_VERSION}_amd64.deb && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
COPY kapacitor.conf /etc/kapacitor/kapacitor.conf  
COPY run.sh /run.sh  
RUN chmod +x /run.sh  
  
EXPOSE 9092  
VOLUME ["/data", "/etc/kapacitor"]  
  
CMD [ "/run.sh" ]

