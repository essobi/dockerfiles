# dir/files  
# conf: /etc/influxdb/influxdb.conf  
# data: /var/lib/influxdb/data  
FROM januswel/centos:7  
MAINTAINER janus_wel <janus.wel.3@gmail.com>  
  
ENV INFLUXDB_LATEST_VERSION 0.9.5.1-1  
ENV RPM_NAME influxdb-${INFLUXDB_LATEST_VERSION}.x86_64.rpm  
ENV RPM_URL https://s3.amazonaws.com/influxdb/${RPM_NAME}  
  
RUN curl -O ${RPM_URL} \  
&& yum -y install ${RPM_NAME} \  
&& rm -f ${RPM_NAME}  
  
CMD /usr/bin/influxd -config /etc/influxdb/influxdb.conf ${INFLUXD_OPTS}  

