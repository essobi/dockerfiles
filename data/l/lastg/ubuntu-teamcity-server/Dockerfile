# docker run -dt -p 8111:8111 --name teamcity-server lastg/ubuntu-teamcity-
server  
FROM library/ubuntu:15.10  
MAINTAINER Last G <last_g@hackerdom.ru>  
  
# TeamCity data is stored in a volume to facilitate container upgrade  
VOLUME ["/var/teamcity"]  
ENV TEAMCITY_DATA_PATH /var/teamcity  
  
# Download and install TeamCity to /opt  
RUN apt-get update && apt-get install -yy --force-yes tar wget openjdk-8-jdk
ca-certificates-java  
RUN update-ca-certificates -f  
  
# Change teamcity version here for update  
ENV TEAMCITY_PACKAGE TeamCity-9.1.4.tar.gz  
ENV TEAMCITY_DOWNLOAD http://download.jetbrains.com/teamcity  
ADD $TEAMCITY_DOWNLOAD/$TEAMCITY_PACKAGE $TEAMCITY_PACKAGE  
RUN tar zxf $TEAMCITY_PACKAGE -C /opt && \  
rm -rf $TEAMCITY_PACKAGE  
  
RUN cd /opt/TeamCity/webapps &&\  
mv ROOT tc  
  
EXPOSE 8111  
CMD ["/opt/TeamCity/bin/teamcity-server.sh", "run"]  

