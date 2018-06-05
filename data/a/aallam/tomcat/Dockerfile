FROM aallam/oracle-java  
MAINTAINER aallam  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV TOMCAT_MAJOR_VERSION=8  
ENV TOMCAT_VERSION=8.5.14  
ENV CATALINA_HOME=/opt/tomcat  
  
WORKDIR /tmp  
  
RUN groupadd tomcat && \  
useradd -s /bin/false -g tomcat -d $CATALINA_HOME tomcat && \  
mkdir $CATALINA_HOME && \  
wget
http://mirrors.standaloneinstaller.com/apache/tomcat/tomcat-$TOMCAT_MAJOR_VERSION/v$TOMCAT_VERSION/bin/apache-
tomcat-$TOMCAT_VERSION.tar.gz && \  
tar xzvf apache-tomcat-8*tar.gz -C $CATALINA_HOME \--strip-components=1 && \  
chown -R tomcat:tomcat $CATALINA_HOME && \  
chmod -R g+r $CATALINA_HOME/conf && \  
chmod g+x $CATALINA_HOME/conf && \  
rm -rf apache-tomcat-$TOMCAT_VERSION.tar.gz  
  
WORKDIR /  
  
ADD tomcat-run.sh /tomcat-run.sh  
ADD settings.xml $CATALINA_HOME/conf/settings.xml  
ADD tomcat-users.xml $CATALINA_HOME/conf/tomcat-users.xml  
ADD context.xml $CATALINA_HOME/webapps/manager/META-INF/context.xml  
RUN chmod 755 /*.sh  
  
EXPOSE 8080  
ENTRYPOINT ["/tomcat-run.sh"]  

