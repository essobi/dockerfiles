FROM debian:jessie  
  
ENV INFLUXDB_URL http://localhost:8086  
ENV DEBIAN_FRONTEND noninteractive  
ENV TELEGRAF_VERSION 0.11.1-1  
RUN apt-get update && \  
apt-get install -y init-system-helpers curl python-pip && \  
curl -O
http://get.influxdb.org/telegraf/telegraf_${TELEGRAF_VERSION}_amd64.deb && \  
dpkg -i telegraf_${TELEGRAF_VERSION}_amd64.deb && rm
telegraf_${TELEGRAF_VERSION}_amd64.deb && \  
pip install envtpl && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
COPY telegraf.conf.tpl /etc/telegraf/telegraf.conf.tpl  
COPY run.sh /run.sh  
RUN chmod +x /run.sh  
  
CMD [ "/run.sh" ]  

