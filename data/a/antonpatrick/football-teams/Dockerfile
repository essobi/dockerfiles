FROM java:8  
VOLUME /tmp  
RUN sh -c 'touch /football-teams.jar'  
ENTRYPOINT
["java","-Djava.security.egd=file:/dev/./urandom","-jar","/football-
teams.jar"]

