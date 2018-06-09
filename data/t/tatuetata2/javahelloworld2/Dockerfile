FROM java:7  
ENV FOO bar  
WORKDIR /home/root/javahelloworld  
RUN mkdir doc  
RUN mkdir src  
RUN mkdir bin  
  
COPY HelloWorld.java ./src  
RUN javac -d bin src/HelloWorld.java  
ENTRYPOINT ["java", "-cp", "bin", "HelloWorld"]  
  

