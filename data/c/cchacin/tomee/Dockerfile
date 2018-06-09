#  
# Apache TomEE Dockerfile  
#  
# https://github.com/cchacin/dockerfiles/tomee  
#  
# Pull base image.  
FROM dockerfile/java:oracle-java7  
  
RUN apt-get update && \  
apt-get install -yq --no-install-recommends wget pwgen ca-certificates && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
ENV CATALINA_HOME /var/lib/tomee  
  
RUN mkdir ${CATALINA_HOME} && \  
wget -qO- "http://apache.tradebit.com/pub/tomee/tomee-1.7.1/apache-
tomee-1.7.1-plus.tar.gz" \  
| tar -zx --strip-components=1 -C ${CATALINA_HOME}  
  
RUN cd ${CATALINA_HOME}/bin && \  
tar xfz commons-daemon-native.tar.gz && \  
cd commons-daemon-1.0.*-native-src/unix && \  
./configure --with-java=${JAVA_HOME} && \  
make && \  
cp jsvc ../.. && \  
cd ../.. && \  
chmod +x jsvc && \  
rm -rf commons-daemon-1.0.*-native-src  
  
ENV CATALINA_OPTS -java-home ${JAVA_HOME} -debug -pidfile
${CATALINA_HOME}/logs/catalina-daemon.pid -wait 10 -outfile
${CATALINA_HOME}/logs/catalina-daemon.out -classpath
${CATALINA_HOME}/bin/bootstrap.jar:${CATALINA_HOME}/bin/commons-
daemon.jar:${CATALINA_HOME}/bin/tomcat-juli.jar
-Djava.util.logging.config.file=${CATALINA_HOME}/conf/logging.properties
-Djava.util.logging.manager=org.apache.juli.ClassLoaderLogManager
-XX:PermSize=1024M -XX:MaxPermSize=1024M -XX:+PrintGCDetails
-XX:+PrintGCDateStamps -XX:+PrintTenuringDistribution
-XX:+PrintGCApplicationConcurrentTime -XX:+PrintGCApplicationStoppedTime
-Xloggc:${CATALINA_HOME}/logs/gc.log -XX:-OmitStackTraceInFastThrow
-Djava.security.egd=file:/dev/./urandom
-Djava.endorsed.dirs=${CATALINA_HOME}/endorsed
-Dcatalina.base=${CATALINA_HOME} -Dcatalina.home=${CATALINA_HOME}
-Djava.io.tmpdir=${CATALINA_HOME}/temp org.apache.catalina.startup.Bootstrap  
  
#ADD target/*.war ${CATALINA_HOME}/webapps/app.war  
  
RUN touch ${CATALINA_HOME}/logs/catalina-daemon.out  
RUN touch ${CATALINA_HOME}/logs/catalina-daemon.pid  
  
EXPOSE 8080  
  
CMD ${CATALINA_HOME}/bin/jsvc ${CATALINA_OPTS} && tail -f
${CATALINA_HOME}/logs/catalina-daemon.out  
  
#CMD ${CATALINA_HOME}/bin/catalina.sh run  

