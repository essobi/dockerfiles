FROM openjdk:8-jdk-alpine  
  
RUN apk add --no-cache curl unzip  
  
ENV DATACLEANER_VERSION 5.2.2  
RUN mkdir /opt && \  
curl -L
https://github.com/datacleaner/DataCleaner/releases/download/DataCleaner-$DATACLEANER_VERSION/DataCleaner-$DATACLEANER_VERSION.zip
> /opt/datacleaner.zip && \  
unzip /opt/datacleaner.zip -d /opt && \  
rm -f /opt/datacleaner.zip  
  
WORKDIR /opt/DataCleaner  
  
ENTRYPOINT ["java","-jar","/opt/DataCleaner/DataCleaner.jar"]

