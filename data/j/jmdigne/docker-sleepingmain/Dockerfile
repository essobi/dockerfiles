FROM openjdk:7  
COPY . /usr/src/myapp  
WORKDIR /usr/src/myapp  
RUN javac -classpath . dockertests/SleepMain.java  
  
CMD ["java", "dockertests/SleepMain"]  

