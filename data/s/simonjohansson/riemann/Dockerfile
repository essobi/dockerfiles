FROM java:8  
RUN apt-get update && apt-get install -y curl bzip2  
RUN curl https://aphyr.com/riemann/riemann-0.2.8.tar.bz2 | tar -C /opt -xj  
  
VOLUME ["/config"]  
  
EXPOSE 5555  
EXPOSE 5556  
ENTRYPOINT if [ -f /config/riemann.config ]; then
CONF_PATH=/config/riemann.config ; else
CONF_PATH=/opt/riemann-0.2.8/etc/riemann.config ; fi && \  
/opt/riemann-0.2.8/bin/riemann $CONF_PATH

