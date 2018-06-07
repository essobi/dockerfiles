FROM openjdk:alpine AS build-env  
RUN apk add --update --no-cache apache-ant  
ADD . /mdb-sqlite  
WORKDIR /mdb-sqlite  
RUN ant dist  
  
FROM openjdk:alpine  
COPY \--from=build-env /mdb-sqlite/dist/mdb-sqlite.jar /usr/bin/mdb-sqlite.jar  
ENTRYPOINT ["java", "-jar", "/usr/bin/mdb-sqlite.jar"]  

