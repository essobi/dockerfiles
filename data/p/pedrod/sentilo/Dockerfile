FROM debian:8  
MAINTAINER guifipedro  
  
RUN mkdir /opt/sentilo  
WORKDIR /opt/sentilo  
  
# fix source  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
  
RUN apt-get clean && \  
apt-get update && \  
apt-get install -y --no-install-recommends \  
# utilities  
git \  
maven2 \  
openjdk-7-jdk \  
curl \  
# databases  
redis-server \  
mongodb \  
# web server  
tomcat7 \  
# creates default java | src:
http://stackoverflow.com/questions/28937722/supervisord-exit-status-1-not-
expected-running-php-script  
default-jre-headless \  
# manage multiple process in this container  
supervisor  
  
# source code  
RUN git clone https://github.com/sentilo/sentilo.git . && \  
chmod -R +x .  
  
# prepare compile script to run non interactively  
RUN sed -i "s/^read$/#read/" ./scripts/buildSentilo.sh  
# compile sentilo  
RUN ./scripts/buildSentilo.sh  
  
# redis conf  
RUN echo masterauth sentilo >> /etc/redis/redis.conf && \  
echo requirepass sentilo >> /etc/redis/redis.conf  
  
# place mongodb directory for its database. It is configured in docker-
entrypoint.sh  
RUN mkdir /mongodb  
# init file for mongodb  
COPY create-sentilo-user.js /  
  
# put web app to tomcat7  
RUN cp ./sentilo-catalog-web/target/sentilo-catalog-web.war
/var/lib/tomcat7/webapps && \  
chown tomcat7 /var/lib/tomcat7/webapps/sentilo-catalog-web.war && \  
chgrp tomcat7 /var/lib/tomcat7/webapps/sentilo-catalog-web.war  
# appropriate permissions to run this services/daemons with supervisor  
RUN chmod +x \  
./sentilo-platform/sentilo-platform-server/target/appassembler/bin/sentilo-
server \  
./sentilo-agent-alert/target/appassembler/bin/sentilo-agent-alert-server \  
./sentilo-agent-relational/target/appassembler/bin/sentilo-agent-relational-
server  
  
# variables needed to run tomcat7 (catalina.sh) with supervisor`  
ENV NAME tomcat7  
ENV JVM_TMP /tmp/tomcat7-$NAME-tmp  
ENV CATALINA_HOME /usr/share/$NAME  
ENV CATALINA_BASE /var/lib/$NAME  
ENV JAVA_HOME /usr/lib/jvm/default-java  
# supervisor conf  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
# entrypoint  
COPY docker-entrypoint.sh /  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
# Web APP  
EXPOSE 8080  
# REST API  
EXPOSE 8081  

