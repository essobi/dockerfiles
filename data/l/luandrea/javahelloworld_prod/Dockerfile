FROM java:7  
MAINTAINER Andreatta Luca <luca.andreatta@eng.it>  
  
COPY src /home/root/javahelloworld/src  
  
WORKDIR /home/root/javahelloworld  
  
RUN mkdir bin  
  
RUN javac -d bin src/HelloWorld.java  
  
RUN mkdir /opt/temp  
  
ENTRYPOINT ["java", "-cp", "bin", "HelloWorld"]  
  

