FROM alpine as crawler  
  
ENV WAVES_VERSION 0.10.3  
RUN apk add --no-cache --update ca-certificates curl && \  
update-ca-certificates && \  
curl -sLo /waves.jar
"https://github.com/wavesplatform/Waves/releases/download/v${WAVES_VERSION}/waves-
all-${WAVES_VERSION}.jar"  
  
FROM openjdk:9-jre-slim  
  
MAINTAINER Drake <drakeramore91@protonmail.com>  
  
COPY \--from=crawler /waves.jar /waves.jar  
  
EXPOSE 6869 6868  
VOLUME ["/root/waves"]  
  
ENTRYPOINT ["/usr/bin/java", "-jar", "/waves.jar"]  
  
CMD ["/root/waves/waves.conf"]

