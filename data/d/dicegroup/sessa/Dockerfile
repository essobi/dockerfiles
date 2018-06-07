## BUILD  
# build first using maven  
FROM maven:3.3.9-jdk-8 as builder  
# set workdir  
WORKDIR /sessa  
# copy files  
ADD . /sessa  
# install deps  
RUN mvn install -Dmaven.test.skip=true  
# run tests  
RUN mvn test  
# build package  
RUN mvn clean package -Dmaven.test.skip=true  
# copy final app jar  
RUN cp -p $(find target -name 'KeywordSearch-*-bootable-with-spring.jar')
sessa.jar  
  
## RELEASE  
# then run in a lighter jdk base  
FROM openjdk:8-jdk  
# set workdir  
WORKDIR /sessa  
# copy jar from build step  
COPY \--from=builder /sessa/sessa.jar sessa.jar  
# Download data from dbpedia & HAWK  
RUN mkdir -p /sessa/resources  
RUN cd /sessa/resources && \  
wget downloads.dbpedia.org/2016-10/dbpedia_2016-10.nt && \  
wget https://raw.githubusercontent.com/dice-
group/NLIWOD/master/qa.hawk/resources/dbpedia_3Eng_class.ttl && \  
wget https://raw.githubusercontent.com/dice-
group/NLIWOD/master/qa.hawk/resources/dbpedia_3Eng_property.ttl  
RUN cd /sessa/resources && \  
wget downloads.dbpedia.org/2016-10/core-i18n/en/labels_en.ttl.bz2 && \  
bunzip2 labels_en.ttl.bz2  
# set default java flags  
ENV JAVA_OPTS="-Xmx4G"  
# expose port  
EXPOSE 8080  
# assign start command  
ENTRYPOINT ["java", "-jar", "sessa.jar"]  

