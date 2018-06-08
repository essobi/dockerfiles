FROM logstash:latest  
MAINTAINER julius_loman@tempest.sk  
  
RUN mkdir -p /opt/logstash/vendor/jar/jdbc/ && wget
https://jdbc.postgresql.org/download/postgresql-9.4.1208.jre7.jar -O
/opt/logstash/vendor/jar/jdbc/postgresql-9.4-1208-jdbc41.jar && \  
/opt/logstash/bin/plugin install logstash-output-jdbc  

