FROM nesneros/kibana-auth:5.2.2  
RUN echo "xpack.security.enabled: false" >> /etc/kibana/kibana.yml  
  
# See https://github.com/elastic/kibana/issues/6057  
# This step might take a few minutes  
RUN /usr/share/kibana/bin/kibana 2>&1 | grep -m 1 "Optimization of .* complete
in .* seconds"  
  

