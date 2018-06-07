FROM centos:7  
MAINTAINER Jimmi Dyson <jimmidyson@gmail.com>  
CMD ["/run.sh"]  
  
ENV KIBANA_VERSION 4.5.3  
  
RUN curl
https://download.elasticsearch.org/kibana/kibana/kibana-${KIBANA_VERSION}-linux-x64.tar.gz
| tar xzv -C /opt && \  
ln -s /opt/kibana* /opt/kibana4 && \  
/opt/kibana4/bin/kibana plugin -i kibana/timelion && \  
chmod 777 /opt/kibana4/config/ /opt/kibana4/optimize/ && \  
chmod 666 /opt/kibana4/config/kibana.yml
/opt/kibana4/optimize/.babelcache.json  
  
ADD run.sh /run.sh  
  
USER nobody  

