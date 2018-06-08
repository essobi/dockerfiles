FROM java:7  
ENV FOO bar  
RUN mkdir -p /home/docker/javahelloworld  
WORKDIR /home/docker/javahelloworld  
RUN mkdir -p /home/docker/javahelloworld/bin  
COPY src /home/docker/javahelloworld/src  
RUN javac -d bin src/HelloWorld.java  
RUN apt-get -y install wget  
ENTRYPOINT ["java", "-cp", "bin", "HelloWorld"]  
  

