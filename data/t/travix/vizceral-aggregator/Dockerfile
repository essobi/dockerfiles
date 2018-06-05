FROM travix/base-alpine:3.5  
MAINTAINER Travix  
  
ENV CONFIG_PATH=/usr/src/app/config.json \  
VIZCERAL_VERSION=1.0.11  
WORKDIR /usr/src/app  
  
RUN apk add --update git curl openjdk8 \  
&& mkdir -p /usr/src/app \  
&& curl -OL https://github.com/OskarKjellin/vizceral-
hystrix/releases/download/v${VIZCERAL_VERSION}/vizceral-
hystrix-${VIZCERAL_VERSION}.jar  
  
COPY config.json config.json  
  
CMD java -jar /usr/src/app/vizceral-hystrix-${VIZCERAL_VERSION}.jar
${CONFIG_PATH}  

