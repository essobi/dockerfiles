FROM java  
COPY src /home/java/src/  
WORKDIR /home/java  
RUN mkdir bin  
RUN javac -d bin src/Hello.java  
ENTRYPOINT ["java", "-cp", "bin", "Hello"]  

