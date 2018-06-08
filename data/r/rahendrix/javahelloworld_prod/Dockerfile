#base install image  
FROM java:7  
MAINTAINER ross.a.hendrix@accenture.com  
  
#copy java hello world files  
COPY src /home/root/javahelloworld/src  
WORKDIR /home/root/javahelloworld  
RUN mkdir bin  
RUN javac -d bin src/HelloWorld.java  
RUN apt-get update && apt-get install -y curl  
ENTRYPOINT ["java","-cp", "bin", "HelloWorld"]  
ENV FOO bar  
  
  

