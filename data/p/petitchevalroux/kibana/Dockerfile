FROM debian:stable  
MAINTAINER Patrick Poulain <docker@m41l.me>  
  
RUN apt-get update  
RUN apt-get install -y wget  
# INSTALLATION  
## Kibana  
RUN \  
wget --no-check-certificate -O kibana.tar.gz
https://download.elasticsearch.org/kibana/kibana/kibana-4.0.0-linux-x64.tar.gz
&& \  
tar xzf kibana.tar.gz -C /opt && \  
ln -s /opt/kibana-4.0.0-linux-x64 /opt/kibana  
  
# CLEANING  
RUN apt-get -y autoremove && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# CONFIGURATION  
## Kibana  
RUN sed -i 's/"http:\/\/localhost:9200"/"http:\/\/elasticsearch:9200"/'
/opt/kibana/config/kibana.yml  
  
EXPOSE 5601  
CMD [ "/opt/kibana/bin/kibana" ]

