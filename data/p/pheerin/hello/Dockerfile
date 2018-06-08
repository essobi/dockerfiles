FROM openjdk:8-jdk  
WORKDIR ./  
ADD ./ ./  
RUN javac -cp src/ src/Main.java  
CMD java -cp ./src Main  

