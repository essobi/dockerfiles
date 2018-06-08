FROM tomcat:8.0-jre8-alpine  
  
RUN rm -rf /usr/local/tomcat/webapps/*  
  
WORKDIR /usr/local/roller  
RUN wget -O roller.tar.gz http://www-
us.apache.org/dist/roller/roller-5.1/v5.1.2/roller-
release-5.1.2-standard.tar.gz  
RUN tar -xf roller.tar.gz  
RUN ln -s roller-release-*/ release  
  
WORKDIR /usr/local/roller  
RUN cp release/webapp/roller.war /usr/local/tomcat/webapps/ROOT.war  
RUN mkdir -p data/mediafiles data/searchindex  
  
WORKDIR /usr/local/tomcat/lib  
RUN wget -O mysql.jar http://repo2.maven.org/maven2/mysql/mysql-connector-
java/5.1.43/mysql-connector-java-5.1.43.jar  
RUN wget http://repo2.maven.org/maven2/javax/mail/mail/1.4.1/mail-1.4.1.jar  
RUN wget
http://repo2.maven.org/maven2/javax/activation/activation/1.1.1/activation-1.1.1.jar  
  
ADD entry-point.sh /usr/local/tomcat/bin  
  
# ensure root can read and write files in Tomcat dir  
RUN chgrp -R 0 /usr/local/tomcat  
RUN chmod -R g+rw /usr/local/tomcat  
  
WORKDIR /usr/local/tomcat  
  
ENTRYPOINT /usr/local/tomcat/bin/entry-point.sh

