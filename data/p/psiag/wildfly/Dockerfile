FROM psiag/oracle-java:8u131  
  
RUN groupadd -r jboss -g 1000 && useradd -u 1000 -r -g jboss -m -d /opt/jboss
-s /sbin/nologin -c "JBoss user" jboss  
  
USER jboss  
  
WORKDIR /opt/jboss  
  
# Expose the ports we're interested in  
EXPOSE 8080 9990 8787  
ENV JBOSS_HOME=/opt/jboss/wildfly WILDFLY_VERSION=11.0.0.Final  
  
RUN curl
http://download.jboss.org/wildfly/$WILDFLY_VERSION/wildfly-$WILDFLY_VERSION.tar.gz
| tar zx && \  
mv wildfly-$WILDFLY_VERSION wildfly  
  
# Set the default command to run on boot  
# This will boot WildFly in the standalone mode and bind to all interface  
CMD ["/opt/jboss/wildfly/bin/standalone.sh", "-b", "0.0.0.0", "-bmanagement",
"0.0.0.0", "--debug"]  

