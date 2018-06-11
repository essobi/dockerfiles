# hoettle: we need to use this image rather than the openjdk:8u131-jdk-alpine  
# image since the KPL requires glibc as well...  
FROM frolvlad/alpine-oraclejdk8:full  
  
# ...and we included libuuid in the installation step due to the KPL  
# requiring it (and Alpine Linux not having it by default). The lack of this  
# library causes unbounded memory consumption and the container dies _very_  
# quickly.  
# See https://github.com/awslabs/amazon-kinesis-producer/issues/86 and  
# https://github.com/awslabs/amazon-kinesis-producer/issues/158  
RUN apk add --no-cache bash curl tini py-pip python \  
libuuid && \  
pip install --no-cache-dir --upgrade pip awscli && \  
curl -sLo /newrelic.jar https://s3.amazonaws.com/unlockd-releases/newrelic-
agent/3.47.0/newrelic.jar && \  
curl -sLo /newrelic.yml https://s3.amazonaws.com/unlockd-releases/newrelic-
agent/3.47.0/newrelic.yml  
  
ENV JAVA_OPTS -XX:+UnlockExperimentalVMOptions
-XX:+UseCGroupMemoryLimitForHeap -XX:MaxRAMFraction=1  
ENTRYPOINT ["/sbin/tini", "--", "/docker-entrypoint.sh"]  
CMD ["start"]  
EXPOSE 8080  

