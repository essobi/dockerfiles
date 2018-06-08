FROM java:7  
RUN apt-get update  
WORKDIR /home/instructor/Desktop/myjavaimage  
COPY src/HelloWorld.java /home/instructor/Desktop/myjavaimage/src/  
RUN mkdir bin  
RUN javac -d bin src/HelloWorld.java  
RUN apt-get install -y vim  
ENTRYPOINT ["java","-cp", "bin", "HelloWorld"]  

