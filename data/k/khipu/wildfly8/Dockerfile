FROM khipu/java8:latest  
MAINTAINER developers@khipu.com  
  
ENV WILDFLY_VERSION 8.2.0.Final  
ENV JBOSS_HOME /opt/wildfly  
  
RUN groupadd -r -g 2100 wildfly && \  
useradd -r -u 2100 -g wildfly -d /opt/wildfly -s /sbin/nologin -c "WildFly
user" wildfly  
  
RUN mkdir /opt/wildfly-$WILDFLY_VERSION  
  
RUN cd /opt && curl
http://download.jboss.org/wildfly/$WILDFLY_VERSION/wildfly-$WILDFLY_VERSION.tar.gz
| tar zx && \  
chown -R wildfly:wildfly /opt/wildfly-$WILDFLY_VERSION  
  
RUN ln -s /opt/wildfly-$WILDFLY_VERSION /opt/wildfly && \  
chown -R wildfly:wildfly /opt/wildfly  
  
EXPOSE 8080 9990  
USER wildfly  
  
ENV LAUNCH_JBOSS_IN_BACKGROUND 1  
CMD ["/opt/wildfly/bin/standalone.sh", "-b", "0.0.0.0", "-bmanagement",
"0.0.0.0"]  

