FROM ubuntu:latest  
MAINTAINER Gary Cornelius <gary.cornelius@rapport.net>  
  
#
--------------------------------------------------------------------------------  
# Linux environment  
#
--------------------------------------------------------------------------------  
# https://influxdb.com/download/#  
# staging v1 > v2 > test > latest influxdb_0.9.5_amd64.deb  
# influxdb 0.9.3 > 0.9.5-s3 > 0.9.5.1 > nightly
https://s3.amazonaws.com/influxdb/influxdb_0.9.5_amd64.deb  
# telegraf 0.1.7 > 0.1.9 > 0.2.3 >
http://get.influxdb.org/telegraf/telegraf_0.2.3_amd64.deb  
# chronograf 0.1.0 > 0.1.0 > 0.2.0 > 0.3.0 >
https://s3.amazonaws.com/get.influxdb.org/chronograf/chronograf_0.3.0_amd64.deb  
ENV DEBIAN_FRONTEND noninteractive  
ENV INFLUXDB_DATABASE_DEFAULT r  
ENV INFLUXDB_ADMIN_USER root  
ENV INFLUXDB_ADMIN_PASS root  
ENV INFLUXDB_VERSION 0.9.5.1  
ENV TELEGRAF_VERSION 0.2.3  
ENV CHRONOGRAF_VERSION 0.3.0  
# ENV SERVER_IP 127.0.0.1  
ENV SERVER_IP 52.19.166.35  
ENV SERVER_HOST localhost  
  
  
# Update the repository and install system utilities required  
RUN apt-get update \  
&& apt-get install curl -y  
  
#
--------------------------------------------------------------------------------  
# Infuxdb: https://influxdb.com/docs  
# Logs: /var/log/supervisor/influxdb.log  
# Data: /opt/influxdb/data  
# Persistent Data: /ecs/influxdb-data  
#
--------------------------------------------------------------------------------  
# STEP 1: Download software, install and remove installer  
RUN curl -s -o /home/influxdb_${INFLUXDB_VERSION}_amd64.deb
https://s3.amazonaws.com/influxdb/influxdb_${INFLUXDB_VERSION}_amd64.deb \  
&& dpkg -i /home/influxdb_${INFLUXDB_VERSION}_amd64.deb \  
&& rm /home/influxdb_${INFLUXDB_VERSION}_amd64.deb \  
&& rm -rf /var/lib/apt/lists/*  
  
# STEP 2: Delete default config file, create a new one and change
configuration settings  
# RUN rm /etc/opt/influxdb/influxdb.conf  
# RUN /opt/influxdb/influxd config > /etc/opt/influxdb/influxdb.conf  
# /usr/lib/influxdb/scripts/ /usr/bin/influxd /etc/influxdb/influxdb.conf  
RUN rm /etc/influxdb/influxdb.conf  
RUN /usr/bin/influxd config > /etc/influxdb/influxdb.conf  
  
RUN sed -i -u "s#dir = \"/root/.influxdb/meta\"#dir =
\"/opt/influxdb/meta\"#g" /etc/influxdb/influxdb.conf  
RUN sed -i -u "s#hostname = \"localhost\"#hostname = \"${SERVER_IP}\"#g"
/etc/influxdb/influxdb.conf  
RUN sed -i -u "s#dir = \"/root/.influxdb/data\"#dir =
\"/opt/influxdb/data\"#g" /etc/influxdb/influxdb.conf  
RUN sed -i -u "s#wal-dir = \"/root/.influxdb/wal\"#wal-dir =
\"/var/opt/influxdb/wal\"#g" /etc/influxdb/influxdb.conf  
RUN mkdir -p /opt/influxdb/hh  
RUN sed -i -u "s#dir = \"/root/.influxdb/hh\"#dir = \"/opt/influxdb/hh\"#g"
/etc/influxdb/influxdb.conf  
  
#
--------------------------------------------------------------------------------  
# Telegraf  
# Logs: /var/log/supervisor/telegraf.log  
#
--------------------------------------------------------------------------------  
# STEP 1: Download software, install and tidy up  
RUN curl -s -o /home/telegraf_${TELEGRAF_VERSION}_amd64.deb
http://get.influxdb.org/telegraf/telegraf_${TELEGRAF_VERSION}_amd64.deb \  
&& dpkg -i /home/telegraf_${TELEGRAF_VERSION}_amd64.deb \  
&& rm /home/telegraf_${TELEGRAF_VERSION}_amd64.deb \  
&& rm -rf /var/lib/apt/lists/*  
  
# STEP 2: Delete default config file, create a new one and change
configuration settings  
RUN rm /etc/opt/telegraf/telegraf.conf  
RUN /opt/telegraf/telegraf -sample-config > /etc/opt/telegraf/telegraf.conf  
  
# outputs > datadog : Comment out  
RUN sed -i -u "s#\\[outputs.datadog\\]#\\#\ [outputs.datadog\\]#g"
/etc/opt/telegraf/telegraf.conf  
RUN sed -i -u "s#apikey = \"my-secret-key\"#\\# apikey = \"my-secret-key\"#g"
/etc/opt/telegraf/telegraf.conf  
  
# outputs > outputs.influxdb : Change server IP, change default database name
and uncomment username and password.  
RUN sed -i -u "s#url = \"http://localhost:8086\"#url =
\"http://${SERVER_IP}:8086\"#g" /etc/opt/telegraf/telegraf.conf  
RUN sed -i -u "s#database = \"telegraf\"#database =
\"${INFLUXDB_DATABASE_DEFAULT}\"#g" /etc/opt/telegraf/telegraf.conf  
RUN sed -i -u "s#\\# username = \"telegraf\"#username = \"root\"#g"
/etc/opt/telegraf/telegraf.conf  
RUN sed -i -u "s#\\# password = \"metricsmetricsmetricsmetrics\"#password =
\"root\"#g" /etc/opt/telegraf/telegraf.conf  
  
# outputs > outputs.kafka : Comment out Kafka, brokers and topic  
RUN sed -i -u "s#\\[outputs.kafka\\]#\\#\ [outputs.kafka\\]#g"
/etc/opt/telegraf/telegraf.conf  
RUN sed -i -u "s#brokers = \\[\"localhost:9092\"\\]#\\# brokers =
\\[\"localhost:9092\"\\]#g" /etc/opt/telegraf/telegraf.conf  
RUN sed -i -u "s#topic = \"telegraf\"#\\# topic = \"telegraf\"#g"
/etc/opt/telegraf/telegraf.conf  
  
# disque : Comment out disque and server list  
RUN sed -i -u "s#\\[disque\\]#\\#\ [disque\\]#g"
/etc/opt/telegraf/telegraf.conf  
RUN sed -i -u "s#servers = \\[\"localhost\"\\]#\\# servers =
\\[\"localhost\"\\]#g" /etc/opt/telegraf/telegraf.conf  
  
# elasticsearch : Comment out servers and local  
RUN sed -i -u "s#servers = \\[\"http://localhost:9200\"\\]#\\# servers =
\\[\"http://localhost:9200\"\\]#g" /etc/opt/telegraf/telegraf.conf  
RUN sed -i -u "s#local = true#\\# local = true#g"
/etc/opt/telegraf/telegraf.conf  
  
# exec : Comment out  
RUN sed -i -u "s#\\[exec\\]#\\#\ [exec\\]#g" /etc/opt/telegraf/telegraf.conf  
RUN sed -i -u "s#\\[\\[exec.commands\\]\\]#\\#\ \\[\\[exec.commands\\]\\]#g"
/etc/opt/telegraf/telegraf.conf  
RUN sed -i -u "s#command = \"/usr/bin/mycollector --foo=bar\"#\\# command =
\"/usr/bin/mycollector --foo=bar\"#g" /etc/opt/telegraf/telegraf.conf  
RUN sed -i -u "s#name = \"mycollector\"#\\# name = \"mycollector\"#g"
/etc/opt/telegraf/telegraf.conf  
  
# haproxy : Comment out  
RUN sed -i -u "s#\\[haproxy\\]#\\#\ [haproxy\\]#g"
/etc/opt/telegraf/telegraf.conf  
RUN sed -i -u "s#servers = \\[\"http://myhaproxy.com:1936\",
\"http://anotherhaproxy.com:1936\"\\]#\\# servers =
\\[\"http://myhaproxy.com:1936\", \"http://anotherhaproxy.com:1936\"\\]#g"
/etc/opt/telegraf/telegraf.conf  
  
# kafka : Comment out zookeeperPeers  
RUN sed -i -u "s#zookeeperPeers = \\[\"localhost:2181\"\\]#\\# zookeeperPeers
= \\[\"localhost:2181\"\\]#g" /etc/opt/telegraf/telegraf.conf  
  
# leofs : Comment out servers  
RUN sed -i -u "s#servers = \\[\"127.0.0.1:4021\"\\]#\\# servers =
\\[\"127.0.0.1:4021\"\\]#g" /etc/opt/telegraf/telegraf.conf  
  
# mongodb : Comment out servers  
RUN sed -i -u "s#servers = \\[\"127.0.0.1:27017\"\\]#\\# servers =
\\[\"localhost:27017\"\\]#g" /etc/opt/telegraf/telegraf.conf  
  
# nginx : Comment out  
RUN sed -i -u "s#urls = \\[\"http://loalhost/status\"\\]#\\# urls =
\\[\"http://loalhost/status\"\\]#g" /etc/opt/telegraf/telegraf.conf  
  
# prometheus : Comment out urls  
RUN sed -i -u "s#urls = \\[\"http://localhost:9100/metrics\"\\]#\\# urls =
\\[\"http://localhost:9100/metrics\"\\]#g" /etc/opt/telegraf/telegraf.conf  
  
# rethinkdb : Comment out servers  
RUN sed -i -u "s#servers = \\[\"127.0.0.1:28015\"\\]#\\# servers =
\\[\"127.0.0.1:28015\"\\]#g" /etc/opt/telegraf/telegraf.conf  
  
#
--------------------------------------------------------------------------------  
# Chronograph: https://influxdb.com/chronograf-download/index.html  
# Logs: /var/log/supervisor/chronograf.log  
#
--------------------------------------------------------------------------------  
# STEP 1: Download software, install and tidy up  
RUN curl -s -o /home/chronograf_${CHRONOGRAF_VERSION}_amd64.deb
https://s3.amazonaws.com/get.influxdb.org/chronograf/chronograf_${CHRONOGRAF_VERSION}_amd64.deb
\  
&& dpkg -i /home/chronograf_${CHRONOGRAF_VERSION}_amd64.deb \  
&& rm /home/chronograf_${CHRONOGRAF_VERSION}_amd64.deb \  
&& rm -rf /var/lib/apt/lists/*  
  
# STEP 2: Configure software  
RUN sed -i -u "s#user=\"chronograf\"#user=\"root\"#g" /etc/default/chronograf  
RUN sed -i -u "s#group=\"chronograf\"#group=\"root\"#g"
/etc/default/chronograf  
RUN sed -i -u "s#nice=\"\"#nice=\"\"\nargs=\"-bind=:10000
-influx=http://${SERVER_IP}:8086\"#g" /etc/default/chronograf  
  
#
--------------------------------------------------------------------------------  
# Supervisor: http://supervisord.org/  
#
--------------------------------------------------------------------------------  
# STEP 1: Download software, install and tidy up  
RUN apt-get update \  
&& apt-get install -y supervisor \  
&& rm -rf /var/lib/apt/lists/*  
  
# STEP 2: Add pre-seeded configuration file to server  
#ADD supervisord.conf /etc/supervisor/conf.d/  
# STEP 2: Create supervisor configure file and configure it for process
management of InfluxDB tools  
RUN echo '[supervisord]\nnodaemon=true\n\n' >
/etc/supervisor/conf.d/supervisord.conf  
# Influxdb process  
# RUN echo
'[program:influxdb]\ndirectory=/opt/influxdb\nuser=root\ncommand=/opt/influxdb/influxd
-config="/etc/opt/influxdb/influxdb.conf"\nstdout_logfile =
/var/log/supervisor/%(program_name)s.log\nstderr_logfile =
/var/log/supervisor/%(program_name)s.log\nautorestart = true\n\n' >>
/etc/supervisor/conf.d/supervisord.conf  
RUN echo
'[program:influxdb]\ndirectory=/opt/influxdb\nuser=root\ncommand=/usr/bin/influxd
-config="/etc/influxdb/influxdb.conf"\nstdout_logfile =
/var/log/supervisor/%(program_name)s.log\nstderr_logfile =
/var/log/supervisor/%(program_name)s.log\nautorestart = true\n\n' >>
/etc/supervisor/conf.d/supervisord.conf  
# Telegraf process  
RUN echo '[program:telegraf]\nuser=root\ncommand=/opt/telegraf/telegraf
-config="/etc/opt/telegraf/telegraf.conf"\nstdout_logfile =
/var/log/supervisor/%(program_name)s.log\nstderr_logfile =
/var/log/supervisor/%(program_name)s.log\nautorestart = true\n\n' >>
/etc/supervisor/conf.d/supervisord.conf  
# Chronograf process  
RUN echo '[program:chronograf]\nuser=root\ncommand=/opt/chronograf/chronograf
-config="/etc/default/chronograf" -bind=":10000"
-influx="http://52.19.166.35:8086"\nstdout_logfile =
/var/log/supervisor/%(program_name)s.log\nstderr_logfile =
/var/log/supervisor/%(program_name)s.log\nautorestart = true\n\n' >>
/etc/supervisor/conf.d/supervisord.conf  
# Create ${INFLUXDB_DATABASE_DEFAULT} database  
RUN echo '[program:createdatabase]\ncommand=bash -c "sleep 5 && exec
/opt/influxdb/influx -host '"'"'52.19.166.35'"'"' -username root -password
root -execute '"'"'CREATE DATABASE r'"'"'"\nstdout_logfile =
/var/log/supervisor/%(program_name)s.log\nstderr_logfile =
/var/log/supervisor/%(program_name)s.log\nautorestart=false\n\n' >>
/etc/supervisor/conf.d/supervisord.conf  
  
#
--------------------------------------------------------------------------------  
# Docker: https://www.docker.com/  
#
--------------------------------------------------------------------------------  
# Expose Ports 8083=http, 8086=admin, 10000=chonograf  
EXPOSE 8083 8086 10000  
# Create a mount point so data can persist when container is stopped # not
implemented yet...  
VOLUME ["/data"]  
  
CMD ["/usr/bin/supervisord", "-n", "-c",
"/etc/supervisor/conf.d/supervisord.conf"]  

