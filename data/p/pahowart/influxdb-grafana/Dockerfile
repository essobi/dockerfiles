FROM ubuntu:16.04  
MAINTAINER Paul Howarth  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV LANG C.UTF-8  
# Default versions  
ENV INFLUXDB_VERSION 1.4.2  
ENV GRAFANA_VERSION 4.6.2  
# Database Defaults  
ENV INFLUXDB_GRAFANA_DB datasource  
ENV INFLUXDB_GRAFANA_USER datasource  
ENV INFLUXDB_GRAFANA_PW datasource  
  
# Default Grafana PLUGINS to be installed (comma separated list)  
ENV GF_INSTALL_PLUGINS=grafana-piechart-panel,briangann-gauge-panel  
  
# Fix bad proxy issue  
COPY system/99fixbadproxy /etc/apt/apt.conf.d/99fixbadproxy  
  
# Clear previous sources  
RUN rm /var/lib/apt/lists/* -vf  
  
# Base dependencies  
RUN apt-get -y update && \  
apt-get -y dist-upgrade && \  
apt-get -y --force-yes install \  
apt-utils \  
ca-certificates \  
curl \  
git \  
htop \  
libfontconfig \  
nano \  
net-tools \  
openssh-server \  
supervisor \  
adduser \  
wget && \  
curl -sL https://deb.nodesource.com/setup_7.x | bash - && \  
apt-get install -y nodejs  
  
WORKDIR /root  
  
RUN mkdir -p /var/log/supervisor && \  
mkdir -p /var/run/sshd && \  
echo 'root:root' | chpasswd && \  
sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/'
/etc/ssh/sshd_config && \  
rm -rf .ssh && \  
rm -rf .profile && \  
mkdir .ssh  
  
# SSH login fix and startup  
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd  
ENV NOTVISIBLE "in users profile"  
RUN echo "export VISIBLE=now" >> /etc/profile  
  
EXPOSE 22  
CMD ["/usr/sbin/sshd", "-D"]  
  
# Install InfluxDB  
RUN wget
https://dl.influxdata.com/influxdb/releases/influxdb_${INFLUXDB_VERSION}_amd64.deb
&& \  
dpkg -i influxdb_${INFLUXDB_VERSION}_amd64.deb && rm
influxdb_${INFLUXDB_VERSION}_amd64.deb  
  
# Install Grafana  
RUN wget https://s3-us-west-2.amazonaws.com/grafana-
releases/release/grafana_${GRAFANA_VERSION}_amd64.deb && \  
dpkg -i grafana_${GRAFANA_VERSION}_amd64.deb && rm
grafana_${GRAFANA_VERSION}_amd64.deb  
  
# Cleanup  
RUN apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Configure Supervisord, SSH and base env  
COPY supervisord/supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
# Configure InfluxDB  
COPY influxdb/influxdb.conf /etc/influxdb/influxdb.conf  
COPY influxdb/init.sh /etc/init.d/influxdb  
  
# Configure Grafana  
COPY grafana/grafana.ini /etc/grafana/grafana.ini  
  
RUN chmod 0755 /etc/init.d/influxdb  
  
CMD ["/usr/bin/supervisord"]  

