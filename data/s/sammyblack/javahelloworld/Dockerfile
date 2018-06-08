FROM java:7  
COPY src /home/root/cidocker/src  
WORKDIR /home/root/cidocker  
RUN mkdir bin  
RUN javac -d bin src/test.java  
ENTRYPOINT ["java", "-cp", "bin", "test"]  

