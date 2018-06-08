FROM philippwaller/debian:latest  
  
LABEL org.label-schema.schema-version="1.0" \  
org.label-schema.name=" InfluxDB" \  
org.label-schema.description="InfluxDB"  
  
RUN DEBIAN_FRONTEND=noninteractive \  
&& echo 'deb https://repos.influxdata.com/debian stretch stable' >
/etc/apt/sources.list.d/influxdb.list \  
&& apt-key adv --fetch-keys https://repos.influxdata.com/influxdb.key \  
&& apt-get update && apt-get install -y influxdb \  
&& rm -rf /var/lib/apt/lists/* /tmp/*  
  
COPY overlay/influxdb.conf /etc/influxdb/influxdb.conf  
COPY overlay/entrypoint.sh /entrypoint.sh  
  
EXPOSE 8083 8086  
VOLUME /var/lib/influxdb  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["influxd"]

