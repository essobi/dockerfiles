FROM store/oracle/serverjre:8  
MAINTAINER Scott Butler <scott@itechpros.com>  
  
# Environment variables  
ENV CATALINA_HOME /usr/share/tomcat  
ENV SERVOY_USER_HOME ${SERVOY_USER_HOME:-/home/servoy}  
ENV TOMCAT_VERSION_MAJOR ${TOMCAT_VERSION_MAJOR:-8}  
ENV TOMCAT_VERSION_FULL ${TOMCAT_VERSION_FULL:-8.5.23}  
ENV TOMCAT_USERNAME ${TOMCAT_USERNAME:-tomcatAdmin}  
ENV TOMCAT_PASSWORD ${TOMCAT_PASSWORD:-tomcatPassword!}  
ENV TOMCAT_MAX_FILE_SIZE ${TOMCAT_MAX_FILE_SIZE:-300000000}  
ENV JAVA_XMS ${JAVA_XMS:-128m}  
ENV JAVA_XMX ${JAVA_XMX:-1024m}  
ENV CATALINA_OPTS -Xms${JAVA_XMS} -Xmx${JAVA_XMX}
-DSERVOY_USER_HOME=${SERVOY_USER_HOME}  
ENV TIME_ZONE ${TIME_ZONE:-America/New_York}  
  
# Add RPM for windows fonts  
ADD msttcore-fonts-2.0-3.noarch.rpm msttcore-fonts-2.0-3.noarch.rpm  
  
#Set Timezone  
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
&& \  
  
# OS Updates and base installs that are useful. net-tools is used by
UserManager plugin  
yum update -y && \  
yum install -y \  
wget \  
unzip \  
tar \  
gzip \  
gunzip \  
net-tools \  
curl \  
gettext && \  
  
# Font http://mscorefonts2.sourceforge.net/  
wget https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm &&
\  
rpm -Uvh epel-release-latest-7*.rpm && \  
yum install -y \  
cabextract \  
xorg-x11-font-utils \  
fontconfig &&\  
  
  
# Install envplate templating engine for environment variable substitution  
curl -sLo /usr/local/bin/ep
https://github.com/kreuzwerker/envplate/releases/download/v0.0.8/ep-linux && \  
chmod +x /usr/local/bin/ep && \  
  
# Install Windows fonts, like Arial and Verdana  
#rpm -Uvh msttcore-fonts-2.0-3.noarch.rpm && \  
rpm -i https://downloads.sourceforge.net/project/mscorefonts2/rpms/msttcore-
fonts-installer-2.6-1.noarch.rpm && \  
  
# Cleanup  
yum clean all && \  
  
# Create Servoy Home Dir and make sure we have full access  
mkdir -p $SERVOY_USER_HOME && \  
chmod +rwx $SERVOY_USER_HOME && \  
  
# Add Tomcat  
mkdir $CATALINA_HOME && \  
wget -O $CATALINA_HOME/apache-tomcat.tar.gz http://www-
us.apache.org/dist/tomcat/tomcat-$TOMCAT_VERSION_MAJOR/v$TOMCAT_VERSION_FULL/bin/apache-
tomcat-$TOMCAT_VERSION_FULL.tar.gz && \  
tar -zxvf $CATALINA_HOME/apache-tomcat.tar.gz -C $CATALINA_HOME --strip-
components=1  
# Add custom config files  
ADD tomcat.conf $CATALINA_HOME/conf/  
ADD manager.xml $CATALINA_HOME/conf/Catalina/localhost/  
ADD tomcat-users.xml $CATALINA_HOME/conf/  
ADD web.xml $CATALINA_HOME/webapps/manager/WEB-INF/  
ADD tomcat_start.sh $CATALINA_HOME/  
  
# Make the startup executable  
RUN chmod +x $CATALINA_HOME/tomcat_start.sh  
  
# Define default working directory  
WORKDIR $CATALINA_HOME/webapps  
  
# Open Ports  
EXPOSE 8080  
EXPOSE 8443  
# Substitute Environment variables in the config files and start services
within the custom script  
CMD $CATALINA_HOME/tomcat_start.sh  

