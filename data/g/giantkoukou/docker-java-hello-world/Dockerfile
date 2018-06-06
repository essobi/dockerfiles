FROM openjdk:8u131-jdk-alpine  
COPY src /home/root/javahelloworld/src  
WORKDIR /home/root/javahelloworld  
RUN mkdir bin  
RUN javac -d bin src/HelloWorld.java  
ENV FOO Giant  
ENTRYPOINT ["java", "-cp", "bin", "HelloWorld"]  

