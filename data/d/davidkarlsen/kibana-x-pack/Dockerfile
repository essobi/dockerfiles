FROM docker.elastic.co/kibana/kibana:6.2.4  
label maintainer "David J. M. Karlsen <david@davidkarlsen.com>"  
  
USER root  
RUN \  
echo "xpack.security.enabled: false" >> /usr/share/kibana/config/kibana.yml &&
\  
echo "xpack.graph.enabled: false" >> /usr/share/kibana/config/kibana.yml && \  
echo "xpack.watcher.enabled: false" >> /usr/share/kibana/config/kibana.yml &&
\  
echo "xpack.reporting.enabled: false" >> /usr/share/kibana/config/kibana.yml
&& \  
chown -R kibana:kibana /usr/share/kibana  
USER kibana  
#https://github.com/elastic/kibana/issues/6057  
RUN kibana 2>&1 | grep -m 1 "Optimization of .* complete in .* seconds"  

