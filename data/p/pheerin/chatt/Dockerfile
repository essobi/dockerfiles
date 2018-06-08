FROM openjdk:8-jdk  
WORKDIR ./  
COPY src/ /src/  
RUN ls -la /src/*  
RUN javac -cp src/main/java/ src/main/java/App.java  
CMD java -cp ./src/main/java/ App  

