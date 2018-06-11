FROM java:7  
RUN apt-get update && apt-get install -y vim curl  
COPY JavaHelloWorld.java .  
RUN javac JavaHelloWorld.java  
CMD ["java", "JavaHelloWorld"]  

