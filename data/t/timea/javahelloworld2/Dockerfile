FROM java:7  
COPY src home/root/javahelloworld/src  
WORKDIR home/root/javahelloworld  
RUN mkdir bin  
RUN echo "eat this"  
RUN javac -d bin src/HelloWorld.java  
ENTRYPOINT ["java", "-cp", "bin", "HelloWorld"]  

