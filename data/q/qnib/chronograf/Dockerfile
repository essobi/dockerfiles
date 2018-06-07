FROM qnib/terminal  
  
ENV CHRONO_VER=0.4.0-1  
RUN yum install -y
https://s3.amazonaws.com/get.influxdb.org/chronograf/chronograf-${CHRONO_VER}.x86_64.rpm  
ADD opt/chronograf/config.toml /opt/chronograf/  
ADD etc/supervisord.d/chronograf.ini /etc/supervisord.d/  
ADD etc/consul.d/chronograf.json /etc/consul.d/  
#ADD opt/qnib/influxdb/bin/start.sh /opt/qnib/influxdb/bin/  

