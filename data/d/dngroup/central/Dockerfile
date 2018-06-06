# Media@home web application Docker image  
#  
# VERSION 1.0  
# ~~~~ Image base ~~~~  
FROM java:8u45-jre  
MAINTAINER David Bourasseau <dbourasseau@viotech.net>  
  
  
EXPOSE 9999  
# get the lasted version of dvd2c-central  
ADD
http://142.4.214.75:8081/nexus/service/local/artifact/maven/redirect?r=snapshots&g=com/enseirb/telecom/dngroup/dvd2c&a=dvd2c-central&v=LATEST&c=jar-
with-dependencies dvd2c-central.jar  
  
CMD sleep 10 && java -jar dvd2c-central.jar --db-hostname mongo --db-port
27017  

