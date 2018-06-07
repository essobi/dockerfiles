FROM maven:3.5.3-jdk-8 AS build  
  
ADD . /build  
WORKDIR /build  
  
RUN cd aws-sdk-java/aws-java-sdk-s3 && mvn -Dgpg.skip=true install  
RUN mvn -Dmaven.test.skip=true package  
  
FROM openjdk:8u151-jre-alpine3.7 AS runtime  
  
RUN apk add \--no-cache bash ca-certificates && \  
addgroup -S runtime && \  
adduser -S -G runtime -h /run runtime && \  
mkdir -p /run/target/conf  
  
COPY \--from=build /build/s3s3mirror.sh /run/  
COPY \--from=build /build/target/s3s3mirror-1.2.6-SNAPSHOT.jar /run/target/  
COPY \--from=build /build/target/classes/log4j.xml /run/target/conf/  
  
RUN chown -R root:root /run && \  
chmod -R a-ws /run  
  
WORKDIR /run  
USER runtime  
  
ENTRYPOINT ["./s3s3mirror.sh"]  

