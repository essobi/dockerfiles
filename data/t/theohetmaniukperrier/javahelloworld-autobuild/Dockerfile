FROM java:7  
COPY src /home/root/javahelloworld/src  
  
WORKDIR /home/root/javahelloworld  
  
ENV FOO bar  
RUN mkdir bin  
  
RUN javac -d bin src/HelloWorld.java  
RUN touch toto  
ENTRYPOINT ["java", "-cp", "bin", "HelloWorld"]  
  

