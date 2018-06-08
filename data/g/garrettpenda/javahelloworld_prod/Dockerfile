  
FROM java:7  
COPY src home/root/javahelloworld/src  
WORKDIR /home/root/javahelloworld  
ENV FOO bar  
  
RUN mkdir bin  
Run javac -d bin src/HelloWorld.java  
RUN apt-get update && apt-get install -y vim  
  
ENTRYPOINT ["java","-cp","bin","HelloWorld"]  

