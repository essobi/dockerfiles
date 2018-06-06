FROM ubuntu:16.04  
RUN apt-get update && apt-get install -y nmon htop openjdk-8-jdk phalanx
gnuchess git  
RUN update-ca-certificates -f  
RUN ln -s /usr/games/gnuchess /usr/bin/gnuchess  
RUN ln -s /usr/games/phalanx /usr/bin/phalanx  
  
# Crafty is not included in the default linux distrib, so we comment it out
for now  
#RUN ln -s /usr/games/crafty /usr/bin/crafty  
COPY . /usr/local/chesscorp/  
  
RUN /usr/local/chesscorp/src/main/scripts/docker_build.sh  
  
EXPOSE 80  
VOLUME /data  
VOLUME /runtime  
  
WORKDIR /runtime  
  
ENV CLUB_BASEURL http://chesscorp.org/  
ENV CLUB_DB_URL jdbc:h2:file:/data/chess1  
ENV CLUB_DB_USERNAME chess  
ENV CLUB_DB_PASSWORD chess  
ENV CLUB_DB_TYPE H2  
ENV CLUB_DB_DDL update  
ENV CLUB_PROFILES jobs,bootstrap,swagger  
ENV CLUB_MAIL_HOST localhost  
ENV CLUB_MAIL_PORT 25  
ENV CLUB_MAIL_SENDER contact@mail.chesscorp.org  
ENV CLUB_VALIDATION_REQ false  
ENV JAVA_OPTS -Xmx2G  
  
CMD java \  
${JAVA_OPTS} \  
-Dserver.port=80 \  
-Dspring.datasource.url=${CLUB_DB_URL} \  
-Dspring.datasource.username=${CLUB_DB_USERNAME} \  
-Dspring.datasource.password=${CLUB_DB_PASSWORD} \  
-Dspring.jpa.database=${CLUB_DB_TYPE} \  
-Dspring.jpa.hibernate.ddl-auto=${CLUB_DB_DDL} \  
-Dspring.profiles.active=${CLUB_PROFILES} \  
-Dspring.mail.host=${CLUB_MAIL_HOST} \  
-Dspring.mail.port=${CLUB_MAIL_PORT} \  
-Dchesscorp.mail.sender=${CLUB_MAIL_SENDER} \  
-Dchesscorp.mail.baseUrl=${CLUB_BASEURL} \  
-Dchesscorp.account.validationRequired=${CLUB_VALIDATION_REQ} \  
-jar /usr/local/chesscorp/target/chess-club-*.jar  

