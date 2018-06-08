FROM java:7  
COPY docker /home/root/javahelloworld/docker  
WORKDIR /home/root/javahelloworld  
RUN mkdir bin  
RUN javac -d bin docker/src/main/java/com/tcs/docker/HelloWorld.java  
  
EXPOSE 8080  
ENTRYPOINT ["java", "-cp", "bin", "com.tcs.docker.HelloWorld"]  
  

