FROM phusion/baseimage:0.9.19  
MAINTAINER hamphh <docker@hampelhh.de>  
  
# Set correct environment variables  
ENV DEBIAN_FRONTEND=noninteractive HOME="/root" TERM=xterm LANG=en_US.UTF-8
LANGUAGE=en_US:en LC_ALL=en_US.UTF-8  
# Set the locale  
RUN locale-gen en_US.UTF-8  
  
# Configure user nobody to match unRAID's settings  
RUN usermod -u 99 nobody && \  
usermod -g 100 nobody && \  
usermod -d /home nobody && \  
chown -R nobody:users /home  
  
#Disable the SSH server  
RUN rm -rf /etc/service/sshd /etc/my_init.d/00_regen_ssh_host_keys.sh  
  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init"]  
  
# Update Image  
RUN apt-get update && apt-get upgrade -y -o Dpkg::Options::="--force-confold"  
  
# Install prerequisits  
RUN apt-get install -qy wget  
  
# InfluxDB  
ENV INFLUXDB_VERSION 1.2.0  
RUN cd /tmp && wget
https://dl.influxdata.com/influxdb/releases/influxdb_${INFLUXDB_VERSION}_amd64.deb
&& \  
dpkg -i influxdb_${INFLUXDB_VERSION}_amd64.deb  
ADD init_influxdb.sh /home/init_influxdb.sh  
RUN chmod +x /home/init_influxdb.sh  
RUN /home/init_influxdb.sh  
  
# Grafana  
ENV GRAFANA_VERSION 4.4.1  
RUN apt-get install -qy adduser libfontconfig  
RUN cd /tmp && wget https://s3-us-west-2.amazonaws.com/grafana-
releases/release/grafana-${GRAFANA_VERSION}.linux-x64.tar.gz && \  
tar xzvf grafana-${GRAFANA_VERSION}.linux-x64.tar.gz && cp -r
grafana-${GRAFANA_VERSION}/ /opt/grafana/  
ADD init_grafana.sh /home/init_grafana.sh  
RUN chmod +x /home/init_grafana.sh  
RUN /home/init_grafana.sh  
  
# Clean up  
RUN apt-get purge -qq wget && apt-get clean && rm -rf /var/lib/apt/lists/*
/tmp/* /var/tmp/*  
  
EXPOSE 3000 8083 8086  
VOLUME /logs \  
/data  
  
# Start Services  
RUN mkdir -p /etc/service/influxdb  
ADD influxdb.sh /etc/service/influxdb/run  
RUN chmod +x /etc/service/influxdb/run  
  
RUN mkdir -p /etc/service/grafana  
ADD grafana.sh /etc/service/grafana/run  
RUN chmod +x /etc/service/grafana/run  

