#  
# dandelion/tomcat:7.0.62-jdk8  
#  
FROM java:8u45-jdk  
MAINTAINER Thibault Duchateau <thibault.duchateau@gmail.com>  
  
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64  
ENV CATALINA_HOME /usr/local/tomcat  
ENV PATH $JAVA_HOME/bin:$CATALINA_HOME/bin:$PATH  
RUN mkdir -p "$CATALINA_HOME"  
WORKDIR $CATALINA_HOME  
  
ENV TOMCAT_MAJOR 7  
ENV TOMCAT_VERSION 7.0.62  
ENV TOMCAT_TGZ_URL
https://www.apache.org/dist/tomcat/tomcat-$TOMCAT_MAJOR/v$TOMCAT_VERSION/bin/apache-
tomcat-$TOMCAT_VERSION.tar.gz  
  
RUN set -x \  
&& curl -fSL "$TOMCAT_TGZ_URL" -o tomcat.tar.gz \  
&& curl -fSL "$TOMCAT_TGZ_URL.asc" -o tomcat.tar.gz.asc \  
&& tar -xvf tomcat.tar.gz --strip-components=1 \  
&& rm bin/*.bat \  
&& rm tomcat.tar.gz*  
  
EXPOSE 8080  
CMD ["catalina.sh", "run"]

