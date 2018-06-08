FROM openjdk:8-jre-alpine  
  
ENV TEAMCITY_VERSION 2017.2.2  
ENV JDBC_DRIVER mysql-connector-java-5.1.40  
ENV TEAMCITY_DATA_PATH /var/lib/teamcity  
  
RUN echo "@edge http://nl.alpinelinux.org/alpine/edge/community" >>
/etc/apk/repositories  
RUN apk --no-cache add\  
curl\  
tomcat-native@edge  
  
# Install teamcity  
RUN mkdir /opt && curl -Ls
https://download.jetbrains.com/teamcity/TeamCity-$TEAMCITY_VERSION.tar.gz |
tar xz -C /opt  
# Install mysql JDBC driver  
RUN mkdir -p $TEAMCITY_DATA_PATH/lib/jdbc $TEAMCITY_DATA_PATH/config\  
&& cd /tmp\  
&& curl -Ls http://dev.mysql.com/get/Downloads/Connector-J/$JDBC_DRIVER.tar.gz
| tar -xz $JDBC_DRIVER/$JDBC_DRIVER-bin.jar\  
&& mv $JDBC_DRIVER/$JDBC_DRIVER-bin.jar $TEAMCITY_DATA_PATH/lib/jdbc/\  
&& rm -r $JDBC_DRIVER  
  
VOLUME /var/lib/teamcity  
  
EXPOSE 8111  
  
ENTRYPOINT /opt/TeamCity/bin/teamcity-server.sh run  

