FROM java:7  
COPY src /home/linux/Dropbox/2/src  
WORKDIR /home/linux/Dropbox/2  
RUN mkdir bin  
RUN javac -d bin src/hellodocker.java  
ENTRYPOINT ["java", "-cp", "bin", "hellodocker"]  
  

