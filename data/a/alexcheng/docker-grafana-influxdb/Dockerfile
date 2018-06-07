FROM centos:centos6  
  
ADD nginx.repo /etc/yum.repos.d/nginx.repo  
RUN yum install -y tar wget python-setuptools nginx  
  
RUN wget http://s3.amazonaws.com/influxdb/influxdb-latest-1.x86_64.rpm  
RUN rpm -ivh influxdb-latest-1.x86_64.rpm  
  
RUN mkdir -p /opt/grafana && cd /opt/grafana && wget
http://grafanarel.s3.amazonaws.com/grafana-1.9.0-rc1.tar.gz && tar xzvf
grafana-1.9.0-rc1.tar.gz --strip 1 && rm grafana-1.9.0-rc1.tar.gz  
  
ADD grafana/config.js /opt/grafana/config.js  
ADD influxdb/run.sh /usr/local/bin/run_influxdb  
RUN chmod 0755 /usr/local/bin/run_influxdb  
  
ADD nginx/nginx.conf /etc/nginx/nginx.conf  
  
RUN easy_install supervisor  
ADD supervisord.conf /etc/supervisord.conf  
  
EXPOSE 80  
EXPOSE 8083  
EXPOSE 8086  
CMD ["/usr/bin/supervisord"]  

