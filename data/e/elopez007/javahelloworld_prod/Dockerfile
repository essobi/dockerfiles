FROM java:8  
MAINTAINER Eliseo Lopez <elopez@legalzoom.com>  
COPY src /home/root/javahelloworld/src  
WORKDIR /home/root/javahelloworld  
RUN mkdir bin && javac -d bin src/HelloWorld.java  
RUN apt-get install -y curl  
ENTRYPOINT ["java", "-cp", "bin", "HelloWorld"]  
ENV FOO bar  

