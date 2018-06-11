FROM java:7  
WORKDIR /home/root/javahelloworld  
COPY HelloWorld.java .  
RUN mkdir bin  
RUN javac HelloWorld.java  
ENTRYPOINT ["java", "HelloWorld"]  
RUN apt-get install wget  

