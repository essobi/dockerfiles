FROM itherz/tomcat8  
  
RUN apt-get -qq update \  
&& apt-get -qq install -y git \  
&& apt-get -qq clean  
  
RUN useradd -m teamcity \  
&& mkdir /logs \  
&& chown -R teamcity:teamcity /apache-tomcat /logs  
  
USER teamcity  
WORKDIR /apache-tomcat  
  
ENV CATALINA_OPTS \  
-Xms1g \  
-Xmx1g \  
-Xss256k \  
-server \  
-XX:+UseCompressedOops \  
-Djsse.enableSNIExtension=true \  
-Djava.awt.headless=true \  
-Dfile.encoding=UTF-8 \  
-Duser.timezone=Europe/Moscow  
  
ENV MAVEN_OPTS \  
-Xms1g \  
-Xmx1g \  
-Xss256k \  
-server \  
-XX:+UseCompressedOops \  
-Djsse.enableSNIExtension=true \  
-Djava.awt.headless=true \  
-Dfile.encoding=UTF-8 \  
-Duser.timezone=Europe/Moscow  
  
  
RUN sed -i 's/connectionTimeout="20000"/connectionTimeout="60000"
useBodyEncodingForURI="true" socket.txBufSize="64000" socket.rxBufSize="64000"
teamcity.options.users.synchronize="true"/' conf/server.xml  
  
EXPOSE 8080  
CMD ["./bin/catalina.sh", "run"]  
  
# ---------------------------------------------------------------------
teamcity  
ENV TEAMCITY_VERSION 10.0.1  
  
RUN curl -LO
http://download.jetbrains.com/teamcity/TeamCity-$TEAMCITY_VERSION.war \  
&& unzip -qq TeamCity-$TEAMCITY_VERSION.war -d webapps/teamcity \  
&& rm -f TeamCity-$TEAMCITY_VERSION.war \  
  
&& rm -f webapps/teamcity/WEB-INF/plugins/clearcase.zip \  
&& rm -f webapps/teamcity/WEB-INF/plugins/mercurial.zip \  
&& rm -f webapps/teamcity/WEB-INF/plugins/eclipse-plugin-distributor.zip \  
&& rm -f webapps/teamcity/WEB-INF/plugins/vs-addin-distributor.zip \  
&& rm -f webapps/teamcity/WEB-INF/plugins/win32-distributor.zip \  
&& rm -fR webapps/teamcity/WEB-INF/plugins/tfs \  
&& rm -fR webapps/teamcity/WEB-INF/plugins/vss \  
&& rm -fR webapps/teamcity/WEB-INF/plugins/dot* \  
&& rm -fR webapps/teamcity/WEB-INF/plugins/visualstudiotest \  
&& rm -fR webapps/teamcity/WEB-INF/plugins/windowsTray \  
  
&& echo '\n<meta name="mobile-web-app-capable" content="yes"/>' >>
webapps/teamcity/WEB-INF/tags/pageMeta.tag \  
&& echo '\n<meta name="theme-color" content="#000"/>' >> webapps/teamcity/WEB-
INF/tags/pageMeta.tag  
  
# ---------------------------------------------------- slack notification
plugin  
ENV SLACK_NOTIFICATION_PLUGIN_VERSION 1.4.4  
  
RUN cd webapps/teamcity/WEB-INF/plugins \  
&& curl -LO
https://github.com/PeteGoo/tcSlackBuildNotifier/releases/download/$SLACK_NOTIFICATION_PLUGIN_VERSION/tcSlackNotificationsPlugin.zip  
RUN cd webapps/teamcity/WEB-INF/plugins \  
&& curl -LO https://bintray.com/artifact/download/jfrog/jfrog-
jars/org/jfrog/teamcity/teamcity-artifactory-plugin/2.2.0/teamcity-
artifactory-plugin-2.2.0.zip  

