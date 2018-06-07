FROM java:7  
WORKDIR /home/root/javahelloworld/bin  
WORKDIR /home/root/javahelloworld  
COPY src src  
RUN javac -d bin src/HelloWorld.java  
ENTRYPOINT ["java", "-cp", "bin", "HelloWorld"]  
ENV FOO bar  

