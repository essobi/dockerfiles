FROM openjdk:8u151-jdk-alpine3.7  
LABEL version="v3.8.6"  
  
ENV RELEASE_TAG v3.8.6  
ENV ARTIFACT hazelcast-kubernetes-bootstrapper-3.8.6.jar  
  
# pulls the hazelcast with bootstrapper jar file  
RUN \  
apk add --update curl ca-certificates tini; apk upgrade; \  
curl -Lskj https://github.com/callstats-io/hazelcast-kubernetes-
bootstrapper/releases/download/$RELEASE_TAG/$ARTIFACT \  
-o /bootstrapper.jar; \  
apk del wget; \  
rm /var/cache/apk/*  
  
EXPOSE 5701 8080  
# copy over the entrypoint file  
ADD docker-entrypoint.sh /usr/local/bin/  
RUN chmod 777 /usr/local/bin/docker-entrypoint.sh  
  
ENTRYPOINT ["/sbin/tini", "--", "/usr/local/bin/docker-entrypoint.sh"]  
CMD ["java", "-jar", "/bootstrapper.jar"]  

