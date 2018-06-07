FROM java  
ENV KIBANA_VERSION=4.2.0  
RUN curl -sSL
https://download.elasticsearch.org/kibana/kibana/kibana-${KIBANA_VERSION}-linux-x64.tar.gz
\  
| tar -xzf - -C /opt \  
&& mv /opt/kibana-${KIBANA_VERSION}-linux-x64 /opt/kibana  
EXPOSE 5601  
CMD ["/opt/kibana/bin/kibana"]  

