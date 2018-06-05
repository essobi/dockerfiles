FROM store/oracle/serverjre:8  
ADD
https://ci.md-5.net/job/BungeeCord/lastSuccessfulBuild/artifact/bootstrap/target/BungeeCord.jar
/bungee/BungeeCord.jar  
  
COPY ./config.yml /bungee/config.yml  
  
WORKDIR /bungee/  
  
EXPOSE 25565  
CMD java -jar BungeeCord.jar  

