FROM alpine:latest  
  
LABEL maintainer="npastorale@gmail.com"  
  
RUN apk update && \  
apk upgrade && \  
apk --no-cache add openjdk8-jre curl wget && \  
mkdir /blynk && \  
mkdir /data && \  
mkdir /config && \  
touch /config/server.properties && \  
curl -s https://api.github.com/repos/blynkkk/blynk-server/releases/latest |
grep "browser_download_url.*java8" | cut -d : -f 2,3 | tr -d \" | wget -i - -O
/blynk/server.jar && \  
apk del curl wget  
  
VOLUME ["/config", "/data/backup"]  
  
EXPOSE 7443 8080 8081 8082 8441 8442 8443 9443  
WORKDIR /data  
ENTRYPOINT ["java", "-jar", "/blynk/server.jar", "-dataFolder", "/data",
"-serverConfig", "/config/server.properties"]  

