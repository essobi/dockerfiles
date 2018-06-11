FROM java:7  
RUN apt-get update && apt-get install -y vim curl  
  
COPY HelloWorld.java .  
RUN javac HelloWorld.java  
  
CMD ["java", "HelloWorld"]

