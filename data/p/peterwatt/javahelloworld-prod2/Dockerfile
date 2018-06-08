FROM java:7  
RUN apt-get update  
RUN apt-get install -y tree && apt-get install -y vim  
COPY src /home/root/javahelloworld/src  
WORKDIR /home/root/javahelloworld  
ENV foo bar  
RUN mkdir bin  
RUN javac -d bin src/HelloWorld.java  
ENTRYPOINT ["java", "-cp", "bin", "HelloWorld"]  

