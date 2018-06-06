FROM java:openjdk-8-jre-alpine  
  
ENV SCALA_VERSION=2.11.8 \  
PATH=$PATH:/opt/scala/bin  
  
RUN apk update && apk upgrade && \  
apk add curl wget bash && \  
mkdir /opt && \  
curl
http://downloads.lightbend.com/scala/${SCALA_VERSION}/scala-${SCALA_VERSION}.tgz
| tar -xvz -C /opt && \  
ln -s /opt/scala-${SCALA_VERSION} /opt/scala  
  
ENTRYPOINT ["bash", "-c"]  

