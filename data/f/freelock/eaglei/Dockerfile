FROM tomcat:7  
MAINTAINER Freelock john@freelock.com  
  
WORKDIR /opt/eaglei  
ENV EAGLE_I_VERSION=4.3.0 REPO_HOME=/opt/eaglei/repo  
RUN DEBIAN_FRONTEND=noninteractive && \  
apt-get update && \  
apt-get install -y libapr1 libtcnative-1  
RUN cd && \  
wget
http://repo.eagle-i.net/nexus/content/repositories/releases/org/eagle-i/eagle-
i-datatools-datamanagement/$EAGLE_I_VERSION/eagle-i-datatools-
datamanagement-$EAGLE_I_VERSION.jar && \  
wget
http://repo.eagle-i.net/nexus/content/repositories/releases/org/eagle-i/eagle-
i-repository-dist/$EAGLE_I_VERSION/eagle-i-repository-dist-$EAGLE_I_VERSION-
dist.zip && \  
unzip eagle-i-repository-dist-$EAGLE_I_VERSION-dist.zip && \  
cp -a repository-$EAGLE_I_VERSION $REPO_HOME  
  
## That was a big download! Let's do our modifications below here to avoid
that...  
RUN rm -Rf $CATALINA_HOME/webapps/ROOT* && \  
cp $REPO_HOME/webapps/ROOT.war $CATALINA_HOME/webapps/ && \  
cp $REPO_HOME/lib/* $CATALINA_HOME/lib/  
  
ENV JAVA_OPTS="-XX:PermSize=64M -XX:MaxPermSize=256M -Xmx1024m"  
RUN echo "org.eaglei.repository.home=$REPO_HOME\n\  
derby.system.home=$REPO_HOME" >> $CATALINA_HOME/conf/catalina.properties  
  
COPY common/eaglei_start.sh /usr/local/bin/eaglei_start.sh  
COPY common/server.xml $CATALINA_HOME/conf/server.xml  
RUN chmod +x /usr/local/bin/eaglei_start.sh && \  
mkdir -p $CATALINA_HOME/conf/Catalina/localhost && \  
unzip -p $CATALINA_HOME/webapps/ROOT.war META-INF/context.xml >
$CATALINA_HOME/conf/Catalina/localhost/ROOT.xml  
  
# Upgrade instructions to update scripts in underlying repo_home  
#  
# Default environment variables for installation scripts  
# Pass these into the docker run command with -e to override  
ENV EAGLE_I_HOME=/opt/eaglei \  
SPARQLER_HOME=/opt/eaglei/sparqler \  
ADMIN_USERNAME=admin \  
ADMIN_PASSWORD=pass \  
SPARQLER_USERNAME=sparqler \  
SPARQLER_PASSWORD=sparq \  
DATABASE_NAME=eagle-i-users.derby \  
REPO_NAMESPACE=http://MY_SITE.data.eagle-i.org/i/ \  
REPO_TITLE="Miskatonic University School of Medicine" \  
REPO_LOGO=/repository/images/logo.png \  
REPO_CSS=/repository/styles/i.css \  
POSTMASTER="admin@example.com" \  
MAIL_HOST="172.16.42.1" \  
MAIL_PORT=25 \  
MAIL_SSL=false  
  
# Now install additional SWEET, INSTITUTION, HELP apps, and Sparqler  
RUN mkdir $EAGLE_I_HOME/conf && \  
wget
http://repo.eagle-i.net/nexus/content/repositories/releases/org/eagle-i/eagle-
i-webapp-sweet/$EAGLE_I_VERSION/eagle-i-webapp-sweet-$EAGLE_I_VERSION.war && \  
cp eagle-i-webapp-sweet-$EAGLE_I_VERSION.war $CATALINA_HOME/webapps/sweet.war
&& \  
wget
http://repo.eagle-i.net/nexus/content/repositories/releases/org/eagle-i/eagle-
i-help/$EAGLE_I_VERSION/eagle-i-help-$EAGLE_I_VERSION.war && \  
cp eagle-i-help-$EAGLE_I_VERSION.war $CATALINA_HOME/webapps/help.war && \  
wget
http://repo.eagle-i.net/nexus/content/repositories/releases/org/eagle-i/eagle-
i-webapp-institution/$EAGLE_I_VERSION/eagle-i-webapp-
institution-$EAGLE_I_VERSION.war && \  
cp eagle-i-webapp-institution-$EAGLE_I_VERSION.war
$CATALINA_HOME/webapps/institution.war && \  
cp $REPO_HOME/webapps/sparqler.war $CATALINA_HOME/webapps/sparqler.war  
  
# Configure Sparqler:  
RUN mkdir sparqler && \  
echo "org.eaglei.sparqler.home=$SPARQLER_HOME" >>
$CATALINA_HOME/conf/catalina.properties  
  
# Configure common apps:  
RUN sed -i
"s+common.loader=\\\$.catalina+common.loader=$EAGLE_I_HOME/conf,\\\$\\\\{catalina+g"
\  
$CATALINA_HOME/conf/catalina.properties && \  
echo "org.eaglei.home=$EAGLE_I_HOME" >>
$CATALINA_HOME/conf/catalina.properties  
  
# Create an assets directory:  
RUN mkdir assets  
  
VOLUME /opt/eaglei  
  
EXPOSE 8009 8443  
CMD ["/usr/local/bin/eaglei_start.sh"]  

