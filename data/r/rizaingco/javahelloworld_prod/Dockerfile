FROM java:7  
WORKDIR /home/root/javahelloworld/  
COPY src /home/root/javahelloworld/src  
RUN mkdir bin  
RUN javac -d bin src/HelloWorld.java  
ENTRYPOINT ["java", "-c", "bin", "Helloworld"]  
ENV FOO bar  
  

