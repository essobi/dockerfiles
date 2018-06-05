# use java:7 as your base image. This image contains the JDK needed to build
and run our application  
FROM java:7  
ENV FOO bar  
  
WORKDIR /home/root/javahelloworld/  
  
# Copy your source file into the container root folder  
COPY src ./src  
  
RUN mkdir bin  
# Add an instruction to compile your code  
RUN javac -d bin src/HelloWorld.java  
RUN touch test  
  
#  
ENTRYPOINT ["java", "-cp", "bin", "HelloWorld"]  
  

