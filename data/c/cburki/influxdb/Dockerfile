FROM debian:jessie  
MAINTAINER Christophe Burki, christophe.burki@gmail.com  
  
ENV INFLUXDB_VERSION 1.3.2  
# Install system requirements  
RUN apt-get update && apt-get install -y \  
curl \  
locales \  
python-pip  
  
# Configure locales and timezone  
RUN locale-gen en_US.UTF-8 en_GB.UTF-8 fr_CH.UTF-8  
RUN cp /usr/share/zoneinfo/Europe/Zurich /etc/localtime  
RUN echo "Europe/Zurich" > /etc/timezone  
  
# Install influxdb  
ADD
https://dl.influxdata.com/influxdb/releases/influxdb_${INFLUXDB_VERSION}_amd64.deb
/tmp/influxdb_amd64.deb  
RUN dpkg -i /tmp/influxdb_amd64.deb  
  
# Influxdb config  
COPY configs/influxdb-noauth.conf /tmp/influxdb-noauth.conf  
COPY configs/influxdb.conf /tmp/influxdb.conf  
  
# Supervisor config  
RUN mkdir /var/log/supervisor  
RUN pip install supervisor  
COPY configs/supervisord.conf /etc/supervisord.conf  
  
# Startup script  
COPY scripts/start.sh /opt/start.sh  
RUN chmod 755 /opt/start.sh  
  
EXPOSE 8083 8086  
CMD ["/bin/bash", "/opt/start.sh"]  

