FROM java:7  
MAINTAINER Julien MEYER <juriexff@gmail.com>  
  
COPY src /home/root/JavaApplication/src  
  
WORKDIR /home/root/JavaApplication  
  
RUN mkdir bin  
  
RUN javac -d bin src/HelloWorld.java  
  
ENTRYPOINT ["java", "-cp", "bin", "HelloWorld"]  

