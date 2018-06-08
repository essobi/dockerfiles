FROM ubuntu:latest  
  
WORKDIR /grain4jmeter  
  
#Keep Package List Updated & software upgraded  
RUN apt-get -y update  
RUN apt-get -y upgrade  
RUN apt-get install -y --no-install-recommends wget curl ca-certificates apt-
transport-https  
  
#======START Grafana======  
ENV GF_SERVER_ROOT_URL http://localhost:3000  
RUN echo "deb https://packagecloud.io/grafana/stable/debian/ jessie main" >>
/etc/apt/sources.list  
RUN curl https://packagecloud.io/gpg.key | apt-key add -  
RUN apt-get -y update  
RUN apt-get -y install grafana  
  
#======END Grafana======  
#======START InfluxDB======  
ENV INFLUXDB_URL http://localhost:8086  
ENV INFLUXDB_DATA_USER root  
ENV INFLUXDB_DATA_PW root  
ENV INFLUXDB_GRAFANA_USER root  
ENV INFLUXDB_GRAFANA_PW root  
ENV ROOT_PW root  
ENV CONFIG_FILE="/etc/influxdb/influxdb.conf"  
ENV API_URL="http://localhost:8086"  
RUN wget https://dl.influxdata.com/influxdb/releases/influxdb_1.3.5_amd64.deb  
RUN dpkg -i influxdb_1.3.5_amd64.deb  
  
ENV INFLUXDB_META_DIR=/var/lib/influxdb/meta \  
INFLUXDB_DATA_DIR=/var/lib/influxdb/data \  
INFLUXDB_DATA_WAL_DIR=/var/lib/influxdb/wal \  
INFLUXDB_HINTED_HANDOFF_DIR=/var/lib/influxdb/hh  
  
COPY influxdb/influxdb.conf /etc/influxdb/influxdb.conf  
  
#======END InfluxDB======  
COPY grafana/create_datasource.json .  
COPY grafana/jmeter_dashboard.json .  
  
COPY scripts/start_grain4jmeter.sh .  
RUN chmod 755 start_grain4jmeter.sh  
  
#Exposing influxdb port for jmeter  
EXPOSE 2003  
#Exposing grafana port  
EXPOSE 3000  
CMD ./start_grain4jmeter.sh ; /bin/bash  

