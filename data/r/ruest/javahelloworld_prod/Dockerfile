FROM java:7  
COPY src /home/root/javahelloworld/src  
ENV FOO bar  
WORKDIR /home/root/javahelloworld  
RUN mkdir bin  
RUN javac -d bin src/HelloWorld.java  
RUN apt-get install -y curl  
ENTRYPOINT ["java", "-cp", "bin", "HelloWorld"]  
  

