FROM java:7  
COPY src /home/root/javahelloworld/src  
WORKDIR /home/root/javahelloworld  
RUN mkdir bin  
ENV FOO bar  
RUN javac -d bin src/HelloWorld.java  
RUN mkdir test  
ENTRYPOINT ["java", "-cp", "bin", "HelloWorld"]  
  

