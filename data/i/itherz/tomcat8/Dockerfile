FROM itherz/java8  
  
# ---------------------------------------------------------------------
tcnative  
ENV APR_VERSION 1.5.2  
ENV TCNATIVE_VERSION 1.1.34  
RUN apt-get update && apt-get install -yq gcc make libssl-dev libpcre++-dev
zlib1g-dev \  
  
&& (curl -L http://www.us.apache.org/dist/apr/apr-$APR_VERSION.tar.gz | gunzip
-c | tar x) \  
&& cd apr-$APR_VERSION \  
&& ./configure \  
&& make install \  
  
&& (curl -L http://www.us.apache.org/dist/tomcat/tomcat-
connectors/native/$TCNATIVE_VERSION/source/tomcat-native-$TCNATIVE_VERSION-
src.tar.gz | gunzip -c | tar x) \  
&& cd tomcat-native-$TCNATIVE_VERSION-src/jni/native \  
&& ./configure --with-java-home=/jdk --with-apr=/usr/local/apr --prefix=/usr \  
&& make install \  
  
&& apt-get autoremove -y cpp gcc make libssl-dev libpcre++-dev zlib1g-dev \  
&& apt-get clean purge \  
&& rm -fR /tmp/* /apr-* /tomcat-native-*  
  
# ----------------------------------------------------------------------
tomcat8  
ENV TOMCAT_VERSION 8.0.36  
RUN (curl -L
http://www.us.apache.org/dist/tomcat/tomcat-8/v$TOMCAT_VERSION/bin/apache-
tomcat-$TOMCAT_VERSION.tar.gz | gunzip -c | tar x) \  
&& mv apache-tomcat-$TOMCAT_VERSION /apache-tomcat \  
&& rm -fR /apache-tomcat/webapps/*  
  
RUN cd /apache-tomcat/conf \  
&& echo '\njava.awt.headless=true' >> catalina.properties  
  
RUN cd /apache-tomcat/lib \  
&& curl -kLO https://jcenter.bintray.com/org/apache/openejb/tomee-
loader/1.7.2/tomee-loader-1.7.2.jar \  
&& curl -kLO
https://jcenter.bintray.com/org/glassfish/main/external/jmxremote_optional-
repackaged/4.1/jmxremote_optional-repackaged-4.1.jar  
  
ADD server.xml /apache-tomcat/conf/  
ADD context.xml /apache-tomcat/conf/  
  
EXPOSE 8080  
CMD ["/apache-tomcat/bin/catalina.sh", "run"]  

