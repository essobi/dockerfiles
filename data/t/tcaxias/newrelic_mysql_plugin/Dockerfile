FROM openjdk:8-alpine  
  
WORKDIR /app  
  
ENV \  
DEPS="wget" \  
APK="apk --update --no-cache" \  
JVM_HEAP="128m" \  
VERSION="2.0.0" \  
NR_KEY=""  
RUN \  
$APK add $DEPS $PKGS && \  
wget --quiet -O- \  
https://github.com/newrelic-
platform/newrelic_mysql_java_plugin/blob/master/dist/newrelic_mysql_plugin-${VERSION}.tar.gz?raw=true
| \  
tar -zx && \  
apk del $DEPS && \  
mv newrelic_mysql_plugin-${VERSION}/config
newrelic_mysql_plugin-${VERSION}/plugin.jar . && \  
rm -rf newrelic_mysql_plugin-${VERSION}  
  
ADD start.sh /app  
  
CMD ["/bin/sh","/app/start.sh"]  

