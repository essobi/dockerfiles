FROM java:8  
COPY src /home/root/javahelloworld/src  
WORKDIR /home/root/javahelloworld  
RUN mkdir bin  
RUN javac -d bin src/HelloWorld.java  
  
ENV FOO BAR  
  
RUN apt-get install -y curl  
ENTRYPOINT ["java", "-cp", "bin", "HelloWorld"]  

