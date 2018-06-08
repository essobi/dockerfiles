FROM docker.elastic.co/kibana/kibana:6.2.1  
COPY kibana.yml /usr/share/kibana/config/kibana.yml  
  
RUN /usr/share/kibana/bin/kibana 2>&1 | grep -m 1 "Optimization of .* complete
in .* seconds"  

