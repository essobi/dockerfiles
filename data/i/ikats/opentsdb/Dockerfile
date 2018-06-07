FROM cloudflare/opentsdb:2.3.0  
LABEL license="Apache License, Version 2.0"  
LABEL copyright="CS Systèmes d'Information"  
LABEL maintainer="contact@ikats.org"  
LABEL version="0.7.39"  
  
RUN mkdir /logs && chmod -R 777 /logs  
  
ADD logback.xml /usr/share/opentsdb/logback.xml  
  
COPY container_init.sh /container_init.sh  
RUN chmod +x /container_init.sh  
  
ENTRYPOINT /container_init.sh  

