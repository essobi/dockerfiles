FROM tomcat:8-alpine  
  
ENV BIRT_VIEWER_WORKING_FOLDER /var/opt/reports  
ENV WEBAPPS_PATH /var/opt/webapps  
ENV BIRT_APP birt  
ENV CONTEXT_PATH ROOT  
  
#Install MS True Type, Ionicons and Font Awesome fonts  
RUN rm -rf /var/cache/apk/* && \  
rm -rf /tmp/* && \  
apk add --update msttcorefonts-installer && \  
update-ms-fonts && \  
mkdir /usr/share/fonts/ko && \  
mkdir /usr/share/fonts/ko/TrueType && \  
cp /usr/share/fonts/truetype/msttcorefonts/*.* /usr/share/fonts/ko/TrueType/
&& \  
wget "https://github.com/ionic-team/ionicons/raw/master/fonts/ionicons.ttf" -P
/usr/share/fonts/ko/TrueType/ && \  
wget "https://github.com/FortAwesome/Font-Awesome/raw/master/web-fonts-with-
css/webfonts/fa-regular-400.ttf" -P /usr/share/fonts/ko/TrueType/ && \  
wget "https://github.com/FortAwesome/Font-Awesome/raw/master/web-fonts-with-
css/webfonts/fa-brands-400.ttf" -P /usr/share/fonts/ko/TrueType/ && \  
wget "https://github.com/FortAwesome/Font-Awesome/raw/master/web-fonts-with-
css/webfonts/fa-solid-900.ttf" -P /usr/share/fonts/ko/TrueType/ && \  
rm -rf /var/cache/apk/* && \  
rm -rf /tmp/*  
  
#Download Birt Runtime  
RUN wget
"http://www.eclipse.org/downloads/download.php?file=/birt/downloads/drops/R-R1-4.7.0-201706222054/birt-
runtime-4.7.0-20170622.zip&mirror_id=1" -O /tmp/birt-runtime.zip && \  
mkdir "/tmp/birt-runtime" && \  
unzip "/tmp/birt-runtime.zip" -d /tmp/birt-runtime && \  
mkdir "$WEBAPPS_PATH" && \  
ls /tmp/birt-runtime/ && \  
mv "/tmp/birt-runtime/WebViewerExample/" "$WEBAPPS_PATH/$BIRT_APP" && \  
rm -rf /tmp/*  
  
#Install MSSQL, PostgreSQL and MySql drivers  
RUN ls "$WEBAPPS_PATH/$BIRT_APP" && \  
wget
"https://download.microsoft.com/download/0/2/A/02AAE597-3865-456C-AE7F-613F99F850A8/sqljdbc_6.0.8112.200_enu.tar.gz"
-P /tmp && \  
wget "https://jdbc.postgresql.org/download/postgresql-42.2.2.jar" -P
"$WEBAPPS_PATH/$BIRT_APP/WEB-INF/lib/" && \  
wget "https://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-
java-5.1.46.tar.gz" -P /tmp && \  
tar -xf "/tmp/sqljdbc_6.0.8112.200_enu.tar.gz" -C
"$WEBAPPS_PATH/$BIRT_APP/WEB-INF/lib/" \--strip-components=3
sqljdbc_6.0/enu/jre8/sqljdbc42.jar && \  
tar -xf "/tmp/mysql-connector-java-5.1.46.tar.gz" -C
"$WEBAPPS_PATH/$BIRT_APP/WEB-INF/lib/" \--strip-components=1 mysql-connector-
java-5.1.46/mysql-connector-java-5.1.46-bin.jar && \  
rm -rf /tmp/*  
  
#Create the reports folder  
RUN mkdir "$BIRT_VIEWER_WORKING_FOLDER" && \  
mkdir "$BIRT_VIEWER_WORKING_FOLDER/samples"  
  
COPY ./templates/reports/*.* "$BIRT_VIEWER_WORKING_FOLDER/samples/"  
  
RUN mkdir "$CATALINA_HOME/conf/Catalina" && \  
mkdir "$CATALINA_HOME/conf/Catalina/localhost/"  
  
COPY ./templates/run.sh /usr/local/bin/run.sh  
COPY ./templates/context.xml "$CATALINA_HOME/template-context.xml"  
  
RUN chmod +x /usr/local/bin/run.sh  
  
RUN rm -rf "${CATALINA_HOME}/webapps/ROOT"  
  
#Modify the web.xml to change the reports folder  
COPY ./templates/web.xml "$WEBAPPS_PATH/$BIRT_APP/WEB-INF/web.xml"  
  
#Modify the landing page  
COPY ./templates/website/ "$WEBAPPS_PATH/$BIRT_APP"  
  
#Map the birt reports folder  
VOLUME $BIRT_VIEWER_WORKING_FOLDER  
  
CMD ["sh", "-c", "/usr/local/bin/run.sh ${CATALINA_HOME} ${CONTEXT_PATH}" ]

