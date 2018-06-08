From java:7  
COPY src /home/docker/myimage/javahelloworld/src  
WORKDIR /home/docker/myimage/javahelloworld  
ENV FOO bar  
  
RUN mkdir bin  
RUN javac -d bin src/HelloWorld.java  
  
ENTRYPOINT ["java", "-cp", "bin", "HelloWorld"]  

