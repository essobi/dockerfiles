FROM logicify/tomcat:latest  
  
USER app  
WORKDIR /srv/apache-tomcat  
  
ENV TEAMCITY_VERSION 2017.2.1  
ENV TEAMCITY_WEBAPP_PATH ROOT  
  
ENV CATALINA_OPTS \  
-Xms768m \  
-Xmx768m \  
-Xss256k \  
-server \  
-XX:+UseCompressedOops \  
-Djsse.enableSNIExtension=false \  
-Djava.awt.headless=true \  
-Dfile.encoding=UTF-8  
  
RUN sed -i 's/connectionTimeout="20000"/connectionTimeout="60000"
useBodyEncodingForURI="true" socket.txBufSize="64000"
socket.rxBufSize="64000"/' conf/server.xml  
  
EXPOSE 8080  
CMD ["./bin/catalina.sh", "run"]  
  
RUN curl -LO
http://download.jetbrains.com/teamcity/TeamCity-$TEAMCITY_VERSION.war  
RUN unzip -qq TeamCity-$TEAMCITY_VERSION.war -d webapps/$TEAMCITY_WEBAPP_PATH
\  
&& curl -o webapps/$TEAMCITY_WEBAPP_PATH/WEB-
INF/lib/postgresql-9.4-1201.jdbc41.jar -L
https://jdbc.postgresql.org/download/postgresql-9.4-1201.jdbc41.jar \  
&& rm -f TeamCity-$TEAMCITY_VERSION.war \  
  
&& rm -f webapps/$TEAMCITY_WEBAPP_PATH/WEB-INF/plugins/clearcase.zip \  
&& rm -f webapps/$TEAMCITY_WEBAPP_PATH/WEB-INF/plugins/mercurial.zip \  
&& rm -f webapps/$TEAMCITY_WEBAPP_PATH/WEB-INF/plugins/eclipse-plugin-
distributor.zip \  
&& rm -f webapps/$TEAMCITY_WEBAPP_PATH/WEB-INF/plugins/vs-addin-
distributor.zip \  
&& rm -f webapps/$TEAMCITY_WEBAPP_PATH/WEB-INF/plugins/win32-distributor.zip \  
&& rm -Rf webapps/$TEAMCITY_WEBAPP_PATH/WEB-INF/plugins/svn \  
&& rm -Rf webapps/$TEAMCITY_WEBAPP_PATH/WEB-INF/plugins/dot* \  
  
&& curl -o webapps/$TEAMCITY_WEBAPP_PATH/WEB-INF/plugins/teamcity-artifactory-
plugin-2.1.5.zip -L http://dl.bintray.com/jfrog/jfrog-
jars/org/jfrog/teamcity/teamcity-artifactory-plugin/2.1.5/teamcity-
artifactory-plugin-2.1.5.zip?direct \  
  
&& echo '<meta name="mobile-web-app-capable" content="yes">' >>
webapps/$TEAMCITY_WEBAPP_PATH/WEB-INF/tags/pageMeta.tag  
  

