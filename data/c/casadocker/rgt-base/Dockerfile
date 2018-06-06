# docker build -t casadocker/rgt-base .  
FROM casadocker/maven:3.5.2 as builder  
  
RUN git clone https://bitbucket.org/tecris/rangitoto  
RUN cd rangitoto && /opt/apache-maven-3.5.2/bin/mvn package  
RUN ls -l /rangitoto/target  
  
FROM anapsix/alpine-java  
RUN mkdir /opt/rangigoto  
COPY \--from=builder /rangitoto/target/rangitoto-1.0.1-SNAPSHOT.jar
/opt/rangitoto/rangitoto-1.0.1-SNAPSHOT.jar  
CMD
["java","-cp","/opt/rangitoto/:/opt/rangitoto/rangitoto-1.0.1-SNAPSHOT.jar","org.rangitoto.Main"]  

