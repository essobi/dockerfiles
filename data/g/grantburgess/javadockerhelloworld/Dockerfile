FROM java:8  
COPY src /home/root/javahelloworld/src  
WORKDIR /home/root/javahelloworld  
RUN mkdir bin  
RUN javac -d bin src/HelloWorld.java  
  
ENV FOO "why am I here"  
RUN apt-get install -y wget  
ENTRYPOINT ["java", "-cp", "bin", "HelloWorld"]  

