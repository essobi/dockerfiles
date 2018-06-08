FROM java:8-jre  
MAINTAINER Lucas Dornelas <lmdornelas@gmail.com>  
  
ADD . /app  
CMD ["java", "-Xmx200m", "-jar", "/app/lucas-mastermind-
game-0.0.1-SNAPSHOT.jar"]  
  
HEALTHCHECK \--interval=10s --timeout=3s CMD curl -f
http://localhost:8888/health || exit 1  
  
EXPOSE 8888  

