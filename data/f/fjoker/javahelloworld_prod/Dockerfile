FROM java:7  
COPY src /home/root/javahelloworld/src  
WORKDIR /home/root/javahelloworld  
RUN mkdir bin  
RUN javac -d bin src/HelloWorld.java  
ENV foo bar  
RUN apt-get install curl -y  
ENTRYPOINT ["java","-cp", "bin", "HelloWorld"]  

