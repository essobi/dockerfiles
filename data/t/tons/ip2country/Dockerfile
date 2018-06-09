FROM openjdk:8-jdk-alpine as builder  
WORKDIR /app  
ADD . /app  
RUN ./gradlew -DskipTests clean bootJar  
  
FROM openjdk:8-jre-alpine  
WORKDIR /app  
# Inspiration http://xmodulo.com/geographic-location-ip-address-command-
line.html  
RUN apk --no-cache add geoip && \  
cd /usr/share/GeoIP && \  
wget
http://geolite.maxmind.com/download/geoip/database/GeoLiteCountry/GeoIP.dat.gz
&& \  
gunzip GeoIP.dat.gz  
  
COPY \--from=builder /app/build/libs/*-SNAPSHOT.jar .  
CMD java -jar *.jar  

