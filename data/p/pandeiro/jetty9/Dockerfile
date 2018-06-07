FROM pandeiro/oracle-jdk8  
MAINTAINER Murphy McMahon <pandeiro.docker@gmail.com>  
  
RUN wget -qO /tmp/jetty.tar.gz \  
'http://eclipse.org/downloads/download.php?file=/jetty/stable-9/dist/jetty-
distribution-9.2.5.v20141112.tar.gz&r=1' \  
&& tar xzf /tmp/jetty.tar.gz -C /opt \  
&& mv /opt/jetty* /opt/jetty \  
&& useradd jetty -U -s /bin/false \  
&& chown -R jetty:jetty /opt/jetty  
  
ADD start-jetty.sh /app/start-jetty  
  
EXPOSE 8080  
ENV JETTY_HOME /opt/jetty  
  
VOLUME ["/opt/jetty/webapps"]  
  
ENTRYPOINT ["/app/start-jetty"]  
  

