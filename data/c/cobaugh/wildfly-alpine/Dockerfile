FROM alpine:3.4  
# Alpine + OpenJDK 8.x + Wildfly 9 docker image  
MAINTAINER Andy Cobaugh <atc135@psu.edu>  
  
ENV WILDFLY_BASE_URL http://download.jboss.org/wildfly  
ENV WILDFLY_VERSION 9.0.2.Final  
  
RUN apk --update --no-cache --virtual=build-dependencies add curl ca-
certificates tar && \  
apk add --no-cache openjdk8 && \  
curl ${WILDFLY_BASE_URL}/${WILDFLY_VERSION}/wildfly-${WILDFLY_VERSION}.tar.gz
> wildfly.tar.gz && \  
tar -xzf wildfly.tar.gz && \  
mv wildfly-${WILDFLY_VERSION} /wildfly && \  
rm -f wildfly.tar.gz && \  
rm -rf /wildfly/welcome-content /wildfly/docs && \  
apk del build-dependencies  
  
ENV LAUNCH_JBOSS_IN_BACKGROUND true  
  
EXPOSE 8080 8009  
CMD [ "/wildfly/bin/standalone.sh", "-b", "0.0.0.0" ]  
  

