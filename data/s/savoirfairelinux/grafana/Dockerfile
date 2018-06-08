FROM debian:jessie  
MAINTAINER Alexandre Viau <alexandre@alexandreviau.net>  
  
ENV GRAFANA_VERSION 2.1.2  
RUN apt-get update && \  
apt-get install -y wget curl && \  
wget
https://grafanarel.s3.amazonaws.com/builds/grafana-${GRAFANA_VERSION}.linux-x64.tar.gz
-O grafana.tar.gz && \  
tar zxf grafana.tar.gz  
  
ADD /grafana.ini grafana.ini  
  
ENV GRAFANA_ROOT_URL %(protocol)s://%(domain)s:%(http_port)s/  
ENV GRAFANA_AUTH_PROXY_ENABLED false  
ENV GRAFANA_AUTH_PROXY_HEADER_NAME X-WEBAUTH-USER  
ADD run.sh /run.sh  
RUN chmod +x /*.sh  
  
CMD ["/run.sh"]  

