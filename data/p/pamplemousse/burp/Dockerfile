FROM openjdk:8-jre  
  
RUN mkdir /burp  
WORKDIR /burp  
  
RUN curl -o burp.jar
"https://portswigger.net/Burp/Releases/Download?productId=100&version=1.7.15&type=Jar"  
  
CMD ["java", "-Djava.awt.headless=false", "-jar", "burp.jar"]  

