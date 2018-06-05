FROM maven:3.3.9-jdk-8  
# set timezone  
RUN cp -f /usr/share/zoneinfo/Asia/Tokyo /etc/localtime  
  
RUN mkdir /app  
WORKDIR /app  
  
ENTRYPOINT ["java", "-jar", "/app/target/WhatDay2-0.0.1-SNAPSHOT.jar"]  
CMD  
# maven build  
COPY pom.xml .  
COPY src src  
RUN mvn package -Dmaven.test.skip=true  

