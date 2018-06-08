FROM kibana:4.6.4  
COPY sense-latest.tar.gz /tmp  
RUN ls -l /tmp  
RUN /opt/kibana/bin/kibana plugin -i sense -u file:///tmp/sense-latest.tar.gz  

