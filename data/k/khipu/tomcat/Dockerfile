FROM khipu/base-alpine  
MAINTAINER developers@khipu.com  
  
ENV JAVA_HOME /usr/lib/jvm/java-1.8-openjdk  
  
ENV TOMCAT_MAJOR 7  
ENV TOMCAT_VERSION 7.0.69  
ENV TOMCAT_SHA1 a8a9f137be01c84908ba6b49820061c82d3d3e2e  
ENV TOMCAT_HOME /opt/tomcat  
  
RUN apk add --no-cache openjdk8  
RUN apk add --no-cache fontconfig  
RUN apk add --no-cache ttf-dejavu  
  
# jvm fixes  
RUN sed -i 's/.*networkaddress.cache.ttl=.*/networkaddress.cache.ttl=5/g'
/usr/lib/jvm/java-1.8-openjdk/jre/lib/security/java.security \  
&& sed -i
's/.*networkaddress.cache.negative.ttl=.*/networkaddress.cache.negative.ttl=5/g'
/usr/lib/jvm/java-1.8-openjdk/jre/lib/security/java.security  
  
RUN curl -O -sSL
https://archive.apache.org/dist/tomcat/tomcat-$TOMCAT_MAJOR/v$TOMCAT_VERSION/bin/apache-
tomcat-$TOMCAT_VERSION.tar.gz \  
&& sha1sum apache-tomcat-$TOMCAT_VERSION.tar.gz | grep $TOMCAT_SHA1 \  
&& tar xzf apache-tomcat-$TOMCAT_VERSION.tar.gz \  
&& mv apache-tomcat-$TOMCAT_VERSION $TOMCAT_HOME \  
&& rm apache-tomcat-$TOMCAT_VERSION.tar.gz \  
&& rm -rf $TOMCAT_HOME/webapps/* \  
&& chown -R khipu:khipu $TOMCAT_HOME  
  
ENTRYPOINT ["su-exec", "khipu", "/opt/tomcat/bin/catalina.sh", "run"]  

