#  
# Dockerfile for JSPWiki running in a tomcat 8 on top of OpenJDK7 on top of
CentoS 7  
# Also install unzip, needed to unzip the default wikipages.  
#  
FROM alpine:3.7  
MAINTAINER Harry Metske <metskem@apache.org>  
RUN apk --update add openjdk7-jre  
#-------------------------------------------------------------  
# Install Tomcat  
#-------------------------------------------------------------  
ADD apache-tomcat.tar.gz /usr/local/  
RUN cd /usr/local && mv apache-tomcat-* apache-tomcat && adduser -D tomcat &&
\  
cd /usr/local && ln -s apache-tomcat tomcat && \  
# remove stuff we don't need  
rm -rf /usr/local/tomcat/bin/*.bat && \  
# provide access to tomcat manager application with user/pw = admin/admin :  
echo -e '<?xml version="1.0" encoding="utf-8"?>\n<tomcat-users>\n<role
rolename="manager-gui"/>\n<role rolename="manager-script"/>\n<role
rolename="manager-jmx"/>\n<role rolename="manager-status"/>\n<role
rolename="admin"/>\n<user username="admin" password="admin"
roles="manager,manager-gui,manager-script,manager-jmx,manager-
status"/>\n</tomcat-users>' > /usr/local/tomcat/conf/tomcat-users.xml  
#-------------------------------------------------------------  
# Install JSPWiki  
#-------------------------------------------------------------  
# add jspwiki war, create JSPWiki webapps dir, unzip it there.  
ADD JSPWiki.war /tmp/jspwiki.war  
# create a directory where all jspwiki stuff will live  
RUN mkdir /var/jspwiki && \  
# first remove default tomcat applications, we dont need them to run jspwiki  
cd /usr/local/tomcat/webapps && rm -rf examples host-manager manager docs ROOT
&& \  
# create subdirectories where all jspwiki stuff will live  
cd /var/jspwiki && mkdir pages logs etc work && mkdir
/usr/local/tomcat/webapps/ROOT && \  
unzip -q -d /usr/local/tomcat/webapps/ROOT /tmp/jspwiki.war && rm
/tmp/jspwiki.war  
#  
ADD jspwiki-wikipages-en-2.10.3-SNAPSHOT.zip /tmp/  
RUN cd /tmp/ && unzip -q jspwiki-wikipages-en-2.10.3-SNAPSHOT.zip && mv
jspwiki-wikipages-en-2.10.3-SNAPSHOT/* /var/jspwiki/pages/ && rm -rf jspwiki-
wikipages-en-2.10.3-SNAPSHOT*  
# move the userdatabase.xml and groupdatabase to /var/jspwiki/etc  
RUN cd /usr/local/tomcat/webapps/ROOT/WEB-INF && mv userdatabase.xml
groupdatabase.xml /var/jspwiki/etc  
# arrange proper logging (jspwiki.use.external.logconfig = true needs to be
set)  
ADD log4j.properties /usr/local/tomcat/lib/log4j.properties  
#  
# make everything owned by tomcat  
RUN chown -R tomcat: /var/jspwiki /usr/local/tomcat/*  
#  
# set default environment entries to configure jspwiki  
ENV LANG en_US.UTF-8  
ENV jspwiki_pageProvider VersioningFileProvider  
ENV jspwiki_fileSystemProvider_pageDir /var/jspwiki/pages  
ENV jspwiki_basicAttachmentProvider_storageDir /var/jspwiki/pages  
ENV jspwiki_workDir /var/jspwiki/work  
ENV jspwiki_xmlUserDatabaseFile /var/jspwiki/etc/userdatabase.xml  
ENV jspwiki_xmlGroupDatabaseFile /var/jspwiki/etc/groupdatabase.xml  
ENV jspwiki_use_external_logconfig true  
ENV jspwiki_templateDir haddock  
ENV jspwiki_jspwiki_frontPage Main  
ENV CATALINA_OPTS -Djava.security.egd=file:/dev/./urandom  
  
# run with user tomcat  
USER tomcat  
  
# make port visible in metadata  
EXPOSE 8080  
#  
# by default we start the Tomcat container when the docker container is
started.  
CMD ["/usr/local/tomcat/bin/catalina.sh","run",
">/usr/local/tomcat/logs/catalina.out"]  

