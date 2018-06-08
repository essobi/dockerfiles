FROM ubuntu:14.04  
RUN apt-get -yqq update && apt-get -yqq upgrade  
RUN apt-get -yqq install tar wget python python-setuptools curl adduser
libfontconfig  
  
RUN wget https://s3.amazonaws.com/influxdb/influxdb_0.9.4.1_amd64.deb -O
influxdb.deb && \  
dpkg -i influxdb.deb  
RUN rm influxdb.deb  
RUN wget https://grafanarel.s3.amazonaws.com/builds/grafana_2.1.3_amd64.deb -O
grafana.deb && \  
dpkg -i grafana.deb  
RUN rm grafana.deb  
  
ADD grafana/config.js /opt/grafana/config.js  
ADD influxdb/run.sh /usr/local/bin/run_influxdb  
RUN chmod a+x /usr/local/bin/run_influxdb  
  
RUN easy_install supervisor  
ADD supervisord.conf /etc/supervisord.conf  
  
EXPOSE 80  
CMD ["/usr/local/bin/supervisord"]  

