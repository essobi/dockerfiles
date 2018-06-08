FROM alpine:3.2  
MAINTAINER Szymon Karnecki <szymon.karnecki@gmail.com>  
  
ENV BUILD_PACKAGES curl-dev ruby-dev build-base  
  
# Update and install base packages  
RUN apk update && apk upgrade && apk add bash $BUILD_PACKAGES  
  
# Install ruby and ruby-bundler  
RUN apk add ruby ruby-io-console ruby-bundler  
  
RUN mkdir /opt  
  
COPY newrelic_pivotal_agent /opt/newrelic_pivotal_agent  
  
WORKDIR /opt/newrelic_pivotal_agent  
  
RUN ["bundle","install"]  
  
ENTRYPOINT ["./pivotal_agent"]  

