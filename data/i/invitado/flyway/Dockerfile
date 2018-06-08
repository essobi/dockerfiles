FROM java:7-jre-alpine  
  
ENV FLYWAY_VERSION 3.2.1  
# Install Flyway.  
RUN mkdir -p /opt \  
&& wget -qO- http://repo1.maven.org/maven2/org/flywaydb/flyway-
commandline/${FLYWAY_VERSION}/flyway-commandline-${FLYWAY_VERSION}.tar.gz |
tar -xzf- -C /opt \  
&& mv /opt/flyway-${FLYWAY_VERSION} /opt/flyway \  
&& echo "flyway.encoding=UTF-8" >> /opt/flyway/conf/flyway.conf  
  
# Mark location for module code.  
RUN mkdir -p /opt/module  
VOLUME /opt/module  
  
# Add entrypoint script.  
COPY ./entrypoint /opt/entrypoint  
RUN chmod 755 /opt/entrypoint  
  
ENTRYPOINT ["/opt/entrypoint"]  
CMD ["info"]  

