FROM frolvlad/alpine-oraclejdk8 as builder  
  
#Configure the develop environment  
RUN apk update  
RUN apk add maven  
  
WORKDIR /develop  
  
ADD pom.xml /develop  
RUN mvn verify --fail-never -P docker-verify  
ADD . /develop  
RUN ./docker/docker.prepare-bundle.sh  
  
FROM frolvlad/alpine-oraclejdk8  
  
#Configure the production environment  
RUN apk update  
RUN apk add mongodb mongodb-tools  
RUN apk add bash  
RUN apk add vim  
  
EXPOSE 8901  
WORKDIR /deploy  
ADD docker/mongodb.conf /deploy  
  
COPY \--from=builder /develop/target/deploy-bundle .  
  
ENTRYPOINT /usr/bin/mongod --config /deploy/mongodb.conf & /bin/bash  

