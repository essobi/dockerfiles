FROM java:8  
COPY src home/root/javahelloworld/src  
  
WORKDIR /home/root/javahelloworld  
RUN mkdir bin  
RUN javac -d bin src/HelloWorld.java  
RUN apt-get install -y curl  
  
ENV FOO bar  
ENTRYPOINT ["java", "-cp", "bin", "HelloWorld"]  
  

