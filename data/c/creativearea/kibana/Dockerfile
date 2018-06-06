FROM ubuntu:14.04  
MAINTAINER CREATIVE AREA  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV KIBANA_VERSION 4.1.0  
ENV KIBANA_PATH /opt/kibana  
  
ADD
https://download.elasticsearch.org/kibana/kibana/kibana-${KIBANA_VERSION}-linux-x64.tar.gz
/tmp/  
  
RUN cd /tmp && \  
tar xzf kibana-*.tar.gz \  
&& rm kibana-*.tar.gz \  
&& mv kibana-* ${KIBANA_PATH}  
  
COPY start.sh /usr/local/bin/start.sh  
RUN chmod ugo+x /usr/local/bin/start.sh  
  
WORKDIR ${KIBANA_PATH}  
  
EXPOSE 5601  
CMD ["/usr/local/bin/start.sh"]  

