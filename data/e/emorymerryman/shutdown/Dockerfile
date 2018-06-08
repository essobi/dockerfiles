FROM alpine:3.4  
COPY install.sh run.sh /opt/shutdown/  
RUN ["/bin/sh", "/opt/shutdown/install.sh"]  
ENTRYPOINT ["/bin/sh", "/opt/shutdown/run.sh"]

