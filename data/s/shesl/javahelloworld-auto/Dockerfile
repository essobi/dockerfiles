FROM java:7  
COPY src /home/root/javahelloworld/src  
WORKDIR /home/root/javahelloworld  
RUN mkdir bin  
RUN javac src/HelloWorld.java  
RUN apt-get update  
  
ENV FOO bar  
  
ENTRYPOINT ["java", "HelloWorld"]  
  

