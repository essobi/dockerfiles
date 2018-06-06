FROM khipu/base-alpine  
MAINTAINER developers@khipu.com  
  
ENV JAVA_HOME /usr/lib/jvm/java-1.8-openjdk  
  
ENV WILDFLY_VERSION 10.1.0.Final  
ENV WILDFLY_SHA1 9ee3c0255e2e6007d502223916cefad2a1a5e333  
ENV JBOSS_HOME /opt/wildfly  
  
RUN apk add --no-cache openjdk8  
  
# jvm fixes  
RUN sed -i 's/.*networkaddress.cache.ttl=.*/networkaddress.cache.ttl=5/g'
/usr/lib/jvm/java-1.8-openjdk/jre/lib/security/java.security \  
&& sed -i
's/.*networkaddress.cache.negative.ttl=.*/networkaddress.cache.negative.ttl=5/g'
/usr/lib/jvm/java-1.8-openjdk/jre/lib/security/java.security  
  
RUN curl -O -sSL
https://download.jboss.org/wildfly/$WILDFLY_VERSION/wildfly-$WILDFLY_VERSION.tar.gz
\  
&& sha1sum wildfly-$WILDFLY_VERSION.tar.gz | grep $WILDFLY_SHA1 \  
&& tar xzf wildfly-$WILDFLY_VERSION.tar.gz \  
&& mv wildfly-$WILDFLY_VERSION $JBOSS_HOME \  
&& rm wildfly-$WILDFLY_VERSION.tar.gz \  
&& chown -R khipu:khipu $JBOSS_HOME  
  
ENV LAUNCH_JBOSS_IN_BACKGROUND true  
  
EXPOSE 8080 9990  
  
ENTRYPOINT ["su-exec", "khipu", "/opt/wildfly/bin/standalone.sh", "-b",
"0.0.0.0"]  

