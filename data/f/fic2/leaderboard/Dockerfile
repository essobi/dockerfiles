FROM java:latest  
  
RUN curl -sL
https://github.com/fic2/FIcontent.Gaming.Enabler.Leaderboard/releases/download/0.2/leaderboard-0.2.tar.gz
| tar zx -C /opt  
  
WORKDIR /opt/leaderboard-0.2  
  
EXPOSE 4567  
CMD ["java","-jar","leaderboard-0.2.jar"]  
  

