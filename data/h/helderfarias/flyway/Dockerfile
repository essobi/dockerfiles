FROM openjdk:7-jdk-alpine  
  
MAINTAINER Helder Farias <helderfarias@gmail.com>  
  
RUN apk add --no-cache curl bash  
  
ENV VERSION=4.2.0  
RUN curl -L https://repo1.maven.org/maven2/org/flywaydb/flyway-
commandline/$VERSION/flyway-commandline-$VERSION.zip > flyway.zip \  
&& unzip flyway.zip \  
&& rm flyway.zip \  
&& mv flyway-$VERSION flyway  
  
VOLUME /flyway/conf  
VOLUME /flyway/sql  
  
WORKDIR /flyway  
  
ENV PATH=/flyway:$PATH  
  
CMD ["sh", "/flyway/flyway"]  

