FROM java:7  
WORKDIR /home/ubuntu/javahelloworld  
RUN mkdir bin  
COPY src /home/ubuntu/javahelloworld/src  
RUN javac -d bin src/HelloWorld.java  
  
ENTRYPOINT ["java", "-cp", "bin", "HelloWorld"]  

