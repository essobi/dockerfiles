FROM jetty:latest  
  
COPY libJNISpice.so /var/lib/jetty/lib/  
RUN set -ex \  
&& mkdir -p /var/opt/lasp/maven/logs \  
&& chown -R jetty:jetty /var/opt/lasp  
VOLUME /var/lib/jetty/webapps  
VOLUME /var/opt/lasp/maven/logs  

