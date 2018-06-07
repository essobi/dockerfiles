FROM debian:latest  
  
# MAINTAINER "Michael Sparenberg"  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
apt-utils \  
sudo \  
nano \  
unzip \  
wget \  
gdebi-core \  
libssl-dev \  
libcurl4-gnutls-dev \  
libsqlite3-dev \  
libspatialite-dev \  
libxdmcp-dev \  
libx11-dev \  
libxcb1-dev \  
libpq-dev \  
adduser \  
libfontconfig \  
openssh-server \  
openssh-client \  
dbus \  
&& apt-get clean  
  
RUN INFLUXDB=influxdb_0.13.0_amd64.deb \  
&& TELEGRAF=telegraf_0.13.2_amd64.deb \  
&& CHRONOGRAF=chronograf_0.13.0_amd64.deb \  
&& KAPACITOR=kapacitor_0.13.1_amd64.deb \  
&& GRFAFANA=grafana_3.1.1-1470047149_amd64.deb \  
&& wget -q --no-check-certificate
https://dl.influxdata.com/influxdb/releases/$INFLUXDB \  
&& gdebi --n --q $INFLUXDB \  
&& rm $INFLUXDB \  
# && wget -q --no-check-certificate
https://dl.influxdata.com/telegraf/releases/$TELEGRAF \  
# && gdebi --n --q $TELEGRAF \  
# && rm $TELEGRAF \  
&& wget -q --no-check-certificate
https://dl.influxdata.com/chronograf/releases/$CHRONOGRAF \  
&& gdebi --n --q $CHRONOGRAF \  
&& rm $CHRONOGRAF \  
&& wget -q --no-check-certificate
https://dl.influxdata.com/kapacitor/releases/$KAPACITOR \  
&& gdebi --n --q $KAPACITOR \  
&& rm $KAPACITOR \  
&& wget -q --no-check-certificate
https://grafanarel.s3.amazonaws.com/builds/$GRFAFANA \  
&& gdebi --n --q $GRFAFANA \  
&& rm $GRFAFANA \  
&& apt-get clean  
  
EXPOSE 3000 8083 8086 10000  
  
RUN echo 'influxd & service grafana-server start & service chronograf start &'
> run_services.sh  
  
CMD ["/bin/bash", "run_services.sh"]  
  

