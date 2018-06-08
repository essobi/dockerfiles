FROM java:7  
WORKDIR /home/root/javahelloworld  
COPY src /home/root/javahelloworld/src  
ENV FOO bar  
RUN mkdir bin  
RUN javac -d bin src/HelloWorld.java  
RUN apt-get update && apt-get install -y vim  
ENTRYPOINT ["java", "-cp", "bin", "HelloWorld"]  

