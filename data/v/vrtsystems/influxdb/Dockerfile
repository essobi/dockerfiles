# vim:set ft=dockerfile:  
# Base on VRT Base image  
FROM vrtsystems/baseimage:develop  
MAINTAINER VRT Engineering <engineering@vrt.com.au>  
  
# add our user and group first to make sure their IDs get assigned  
# consistently, regardless of whatever dependencies get added later  
RUN groupadd -r influxdb && useradd -r -g influxdb influxdb  
  
ENV INFLUX_VERSION 1.3.2  
ENV INFLUX_CONFIG /etc/influxdb/influxdb.conf  
ENV INFLUX_DATA /var/local/influxdb  
  
RUN curl
https://dl.influxdata.com/influxdb/releases/influxdb_${INFLUX_VERSION}_amd64.deb
> /tmp/influxdb_amd64.deb \  
&& dpkg -i /tmp/influxdb_amd64.deb \  
&& cd /etc/influxdb/ && cp influxdb.conf influxdb.conf.orig \  
&& mkdir /var/local/influxdb && chown influxdb:influxdb /var/local/influxdb \  
&& sed -i "s/var\/lib\/influxdb/var\/local\/influxdb/" "$INFLUX_CONFIG" \  
&& mkdir -p /usr/local/etc/docker-influxdb/prestart-init.d \  
&& mkdir -p /usr/local/etc/docker-influxdb/poststart-init.d \  
&& echo "=== Cleaning up ========================" \  
&& rm /tmp/influxdb_amd64.deb \  
&& /usr/local/sbin/docker-cleanup.sh  
  
#ENV PATH /opt/influxdb:$PATH  
COPY env-ini.py /usr/local/sbin/env-ini.py  
  
COPY docker-entrypoint.sh /usr/local/sbin/  
COPY supervisord-postinit.sh /usr/local/sbin/  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
ENV SSL_SUPPORT **False**  
ENV SSL_CERT **None**  
ENV INFLUXDB_REPORTING_DISABLED false  
  
# HTTP API  
EXPOSE 8086  
# HTTPS API  
EXPOSE 8084  
# Raft port (for clustering, don't expose publicly!)  
#EXPOSE 8090  
# Protobuf port (for clustering, don't expose publicly!)  
#EXPOSE 8099  
ENTRYPOINT ["/usr/local/sbin/docker-entrypoint.sh"]  
  
CMD ["supervisor"]  

