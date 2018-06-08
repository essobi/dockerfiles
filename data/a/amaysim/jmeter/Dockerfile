FROM openjdk:8-jre-alpine  
  
ENV JMETER_VERSION 3.2  
ENV JMETER_HOME /opt/jmeter  
ENV JMETER_DOWNLOAD_URL
http://apache.mirror.serversaustralia.com.au//jmeter/binaries/apache-
jmeter-${JMETER_VERSION}.tgz  
  
RUN apk --no-cache update && \  
apk --no-cache add bash ca-certificates curl git less make zip && \  
update-ca-certificates && \  
rm -rf /var/cache/apk/*  
  
RUN mkdir -p ${JMETER_HOME} && \  
curl -L --silent ${JMETER_DOWNLOAD_URL} | tar -xz --strip-components 1 -C
/opt/jmeter  
  
WORKDIR /opt/app  
  
#ENTRYPOINT ["java", "-jar", "/opt/jmeter/bin/ApacheJMeter.jar", "-n", "-t"]  

