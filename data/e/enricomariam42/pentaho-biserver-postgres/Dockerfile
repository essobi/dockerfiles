# Docker image based on enricomariam42/baseimage-java7 and customized pentaho
biserver  
# VERSION 1.0  
FROM enricomariam42/baseimage-java7:latest  
MAINTAINER Enrico Maria Carmona, e.carmona@hsgerardo.org  
  
ENV HOME /root  
ENV TOMCAT_HOME /opt/pentaho/biserver-ce/tomcat  
ENV PENTAHO_HOME /opt/pentaho/biserver-ce  
ENV BASE_REL 5.4  
ENV REV 0.1-130  
ENV DB_TYPE postgresql  
  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init"]  
  
RUN apt-get -qq update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -f -y -q \  
unzip \  
zip  
  
# biserver  
RUN useradd -m pentaho && \  
mkdir /opt/pentaho  
  
RUN chown -Rf pentaho:pentaho /opt/pentaho && \  
su -c "curl -L
http://sourceforge.net/projects/pentaho/files/Business%20Intelligence%20Server/${BASE_REL}/biserver-
ce-${BASE_REL}.${REV}.zip/download -o /opt/pentaho/biserver-ce.zip" pentaho &&
\  
su -c "unzip -q /opt/pentaho/biserver-ce.zip -d /opt/pentaho/" pentaho && \  
rm /opt/pentaho/biserver-ce/promptuser.sh && \  
rm /opt/pentaho/biserver-ce.zip && \  
# Disable daemon mode for Tomcat  
sed -i -e 's/\\(exec ".*"\\) start/\1 run/' /opt/pentaho/biserver-
ce/tomcat/bin/startup.sh  
  
# db configuration files  
ADD v5/pentaho/system/${DB_TYPE}/applicationContext-spring-security-
hibernate.properties /opt/pentaho/biserver-ce/pentaho-
solutions/system/applicationContext-spring-security-hibernate.properties  
ADD v5/pentaho/system/${DB_TYPE}/hibernate-settings.xml /opt/pentaho/biserver-
ce/pentaho-solutions/system/hibernate/hibernate-settings.xml  
ADD v5/pentaho/system/${DB_TYPE}/quartz.properties /opt/pentaho/biserver-
ce/pentaho-solutions/system/quartz/quartz.properties  
ADD v5/pentaho/system/${DB_TYPE}/repository.xml /opt/pentaho/biserver-
ce/pentaho-solutions/system/jackrabbit/repository.xml  
ADD v5/pentaho/system/${DB_TYPE}/postgresql.hibernate.cfg.xml
/opt/pentaho/biserver-ce/pentaho-
solutions/system/hibernate/postgresql.hibernate.cfg.xml  
  
# tomcat configuration files  
ADD v5/tomcat/${DB_TYPE}/context.xml /opt/pentaho/biserver-
ce/tomcat/webapps/pentaho/META-INF/context.xml  
ADD v5/tomcat/web.xml /opt/pentaho/biserver-ce/tomcat/webapps/pentaho/WEB-
INF/web.xml  
  
# turn off jpivot deprecation message  
ADD v5/pentaho/system/pentaho-jpivot-plugin/settings.xml
/opt/pentaho/biserver-ce/pentaho-solutions/system/pentaho-jpivot-
plugin/settings.xml  
  
# update jdbc drivers  
RUN rm -f /opt/pentaho/biserver-ce/tomcat/lib/mysql-* \  
/opt/pentaho/biserver-ce/tomcat/lib/postgresql-* \  
/opt/pentaho/biserver-ce/tomcat/webapps/pentaho/WEB-INF/lib/monetdb-jdbc* && \  
# monetdb  
wget -O /opt/pentaho/biserver-ce/tomcat/lib/monetdb-jdbc-`curl -s
https://clojars.org/repo/monetdb/monetdb-jdbc/maven-metadata.xml | grep -Po
'<release>.*' | grep -Po [0-9\\.]+`.jar
https://clojars.org/repo/monetdb/monetdb-jdbc/`curl -s
https://clojars.org/repo/monetdb/monetdb-jdbc/maven-metadata.xml | grep -Po
'<release>.*' | grep -Po [0-9\\.]+`/monetdb-jdbc-`curl -s
https://clojars.org/repo/monetdb/monetdb-jdbc/maven-metadata.xml | grep -Po
'<release>.*' | grep -Po [0-9\\.]+`.jar && \  
# mysql  
wget -O /opt/pentaho/biserver-ce/tomcat/lib/mysql-connector-java-`curl -s
'https://search.maven.org/solrsearch/select?q=a:%22mysql-connector-
java%22+AND+g:%22mysql%22&wt=json' | grep -Po '"latestVersion":.*?[^\\\\]]",'
| grep -Po '[0-9\\.]+'`.jar
https://search.maven.org/remotecontent?filepath=mysql/mysql-connector-
java/`curl -s 'https://search.maven.org/solrsearch/select?q=a:%22mysql-
connector-java%22+AND+g:%22mysql%22&wt=json' | grep -Po
'"latestVersion":.*?[^\\\\]]",' | grep -Po '[0-9\\.]+'`/mysql-connector-
java-`curl -s 'https://search.maven.org/solrsearch/select?q=a:%22mysql-
connector-java%22+AND+g:%22mysql%22&wt=json' | grep -Po
'"latestVersion":.*?[^\\\\]]",' | grep -Po '[0-9\\.]+'`.jar && \  
# postgres  
wget -O /opt/pentaho/biserver-ce/tomcat/lib/postgresql-`curl -s
'https://search.maven.org/solrsearch/select?q=a:%22postgresql%22+AND+g:%22org.postgresql%22&wt=json'
| grep -Po '"latestVersion":.*?[^\\\\]]",'| grep -Pow
'[0-9\\.\\-]+'`jdbc41.jar
https://search.maven.org/remotecontent?filepath=org/postgresql/postgresql/`curl
-s
'https://search.maven.org/solrsearch/select?q=a:%22postgresql%22+AND+g:%22org.postgresql%22&wt=json'
| grep -Po '"latestVersion":.*?[^\\\\]]",'| grep -Pow
'[0-9\\.\\-]+'`jdbc41/postgresql-`curl -s
'https://search.maven.org/solrsearch/select?q=a:%22postgresql%22+AND+g:%22org.postgresql%22&wt=json'
| grep -Po '"latestVersion":.*?[^\\\\]]",'| grep -Pow
'[0-9\\.\\-]+'`jdbc41.jar && \  
chown -f pentaho:pentaho /opt/pentaho/biserver-ce/tomcat/lib/*  
  
# Install saiku, pivot4j  
RUN wget -O ~/ctools-installer.sh
https://raw.githubusercontent.com/pmalves/ctools-installer/master/ctools-
installer.sh && \  
chmod +x ~/ctools-installer.sh && \  
~/ctools-installer.sh -y -s /opt/pentaho/biserver-ce/pentaho-solutions -w
/opt/pentaho/biserver-ce/tomcat/webapps/pentaho -c saiku && \  
rm ~/ctools-installer.sh* && \  
# Remove Saiku splas screen  
sed -i 's/SplashScreen,!1/Workspace/' /opt/pentaho/biserver-ce/pentaho-
solutions/system/saiku/ui/saiku.min.js && \  
# Remove Saiku "consider upgrading" banner  
echo ".upgrade {\n display: none;\n}" >> /opt/pentaho/biserver-ce/pentaho-
solutions/system/saiku/ui/css/saiku/src/styles.css && \  
# Allow import-export saiku files  
sed -i 's|<entry key="jpeg" value-ref="streamConverter"/>|&\n\t\t\t\t<entry
key="saiku" value-ref="streamConverter"/>|' /opt/pentaho/biserver-ce/pentaho-
solutions/system/importExport.xml && \  
sed -i 's|<value>.xcdf</value>|&\n\t\t\t\t<value>.saiku</value>|'
/opt/pentaho/biserver-ce/pentaho-solutions/system/importExport.xml && \  
sed -i
's|<extension>xreportspec</extension>|&\n\t\t<extension>saiku</extension>|'
/opt/pentaho/biserver-ce/pentaho-
solutions/system/ImportHandlerMimeTypeDefinitions.xml && \  
# Install pivot4j  
su -c "curl -L
http://ci.greencatsoft.com/job/Pivot4J/lastSuccessfulBuild/artifact/pivot4j-pentaho/target/pivot4j-pentaho-1.0-SNAPSHOT-
plugin.tar.gz -o /opt/pentaho/biserver-ce/pentaho-
solutions/system/pivot4j.tar.gz" pentaho && \  
cd /opt/pentaho/biserver-ce/pentaho-solutions/system/ && \  
su -c "tar xzvf pivot4j.tar.gz" pentaho && \  
rm pivot4j.tar.gz && \  
cd / && \  
# Allow import-export pivot4j files  
sed -i 's|<entry key="jpeg" value-ref="streamConverter"/>|&\n\t\t\t\t<entry
key="pivot4j" value-ref="streamConverter"/>|' /opt/pentaho/biserver-
ce/pentaho-solutions/system/importExport.xml && \  
sed -i 's|<value>.xcdf</value>|&\n\t\t\t\t<value>.pivot4j</value>|'
/opt/pentaho/biserver-ce/pentaho-solutions/system/importExport.xml && \  
sed -i
's|<extension>xreportspec</extension>|&\n\t\t<extension>pivot4j</extension>|'
/opt/pentaho/biserver-ce/pentaho-
solutions/system/ImportHandlerMimeTypeDefinitions.xml  
  
# Configure training defaut users  
RUN for i in $(seq 30 -1 1); do \  
sed -i 's|<util:map id="defaultUserRoleMappings">|'"&\n\t\t<entry
key=\"user$i\">\n\t\t\t<util:list>\n\t\t\t\t<ref
bean=\"singleTenantAuthenticatedAuthorityName\"/>\n\t\t\t\t<value>Power
User</value>\n\t\t\t</util:list>\n\t\t</entry>"'|' /opt/pentaho/biserver-
ce/pentaho-solutions/system/defaultUser.spring.xml \  
; done  
  
RUN chown -Rf pentaho:pentaho /opt/pentaho  
  
RUN mkdir /etc/service/pentaho  
ADD run /etc/service/pentaho/run  
RUN chmod +x /etc/service/pentaho/run  
  
# Expose Pentaho port  
EXPOSE 8080  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

