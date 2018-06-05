FROM java:8-jdk  
  
ADD
http://ci.md-5.net/job/BungeeCord/lastSuccessfulBuild/artifact/bootstrap/target/BungeeCord.jar
/app/BungeeCord.jar  
  
WORKDIR /app/  
  
CMD ["java", "-Xmx2G", "-Xincgc", "-jar", "BungeeCord.jar"]  

