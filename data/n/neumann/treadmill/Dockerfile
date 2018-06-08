FROM java:jdk-alpine  
  
ADD . /code  
  
RUN apk add \--update bash curl && \  
cd /code && \  
./sbt assembly && \  
cp /code/target/scala-2.11/*-assembly-*.jar /treadmill.jar && \  
rm -rf /code && \  
rm -rf /root/.sbt/ && \  
rm -rf /root/.ivy2/ && \  
apk del bash curl && \  
rm -rf /var/cache/apk/*  
  
ENTRYPOINT ["/usr/bin/java", "-server", "-jar", "/treadmill.jar"]  

