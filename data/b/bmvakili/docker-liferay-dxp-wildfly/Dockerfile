##  
## Docker image: Liferay DXP -> WildFly (JBoss)  
##  
## Build: docker build -t liferay-dxp-wildfly .  
## Run: docker run -it -p 8080:8080 liferay-dxp-wildfly  
##  
FROM jboss/base-jdk:8  
# ENVIRONMENT  
ENV WILDFLY_VERSION "10.1.0.Final"  
ENV WILDFLY_SHA1 "9ee3c0255e2e6007d502223916cefad2a1a5e333"  
ENV LIFERAY_VERSION "7.0.2 GA3"  
ENV LIFERAY_VERSION_FULL "7.0-ga3-20160804222206210"  
ENV LIFERAY_WAR_SHA1 "3a1a8cd8b5e31c3bdd8c433c6330e8a3cff46251"  
ENV LIFERAY_OSGI_SHA1 "f542dcb943cbb5996879b781592ef2545f13b424"  
ENV LIFERAY_DEPS_SHA1 "22c0d1bd47c5945bd1a365b0e0bec31885dfd97d"  
# PATHS  
ENV DOWNLOAD /tmp/download/  
ENV LIFERAY_HOME /opt/app/liferay/  
ENV WILDFLY_HOME /opt/app/liferay/wildfly  
ENV WILDFLY_STANDALONE_CFG
/opt/app/liferay/wildfly/standalone/configuration/standalone.xml  
  
# DOWNLOAD packages  
RUN mkdir $DOWNLOAD \  
&& cd $DOWNLOAD  
RUN curl -O
"https://download.jboss.org/wildfly/$WILDFLY_VERSION/wildfly-$WILDFLY_VERSION.tar.gz"  
RUN curl -L -O "http://downloads.sourceforge.net/project/lportal/Liferay
Portal/$LIFERAY_VERSION/liferay-ce-portal-$LIFERAY_VERSION_FULL.war"  
RUN curl -L -O "http://downloads.sourceforge.net/project/lportal/Liferay
Portal/$LIFERAY_VERSION/liferay-ce-portal-osgi-$LIFERAY_VERSION_FULL.zip"  
RUN curl -L -O "http://downloads.sourceforge.net/project/lportal/Liferay
Portal/$LIFERAY_VERSION/liferay-ce-portal-
dependencies-$LIFERAY_VERSION_FULL.zip"  
RUN mv *.* $DOWNLOAD  
  
## INSTALLATION: JBOSS WildFly  
USER root  
COPY files /tmp/files  
  
RUN mkdir -p $LIFERAY_HOME \  
&& cd $LIFERAY_HOME \  
&& sha1sum $DOWNLOAD/wildfly-$WILDFLY_VERSION.tar.gz | grep $WILDFLY_SHA1 \  
&& tar xf $DOWNLOAD/wildfly-$WILDFLY_VERSION.tar.gz \  
&& ln -s $LIFERAY_HOME/wildfly-$WILDFLY_VERSION wildfly  
  
## LIFERAY DXP  
RUN mkdir $WILDFLY_HOME/standalone/deployments/ROOT.war \  
&& cd $WILDFLY_HOME/standalone/deployments/ROOT.war \  
&& sha1sum $DOWNLOAD/liferay-ce-portal-$LIFERAY_VERSION_FULL.war | grep
$LIFERAY_WAR_SHA1 \  
&& unzip $DOWNLOAD/liferay-ce-portal-$LIFERAY_VERSION_FULL.war > /dev/null \  
&& touch $WILDFLY_HOME/standalone/deployments/ROOT.war.dodeploy  
RUN cd $LIFERAY_HOME \  
&& sha1sum $DOWNLOAD/liferay-ce-portal-osgi-$LIFERAY_VERSION_FULL.zip | grep
$LIFERAY_OSGI_SHA1 \  
&& unzip $DOWNLOAD/liferay-ce-portal-osgi-$LIFERAY_VERSION_FULL.zip >
/dev/null \  
&& find -name "liferay-ce-portal-osgi*" -exec ln -s {} osgi \;  
RUN mkdir -p $WILDFLY_HOME/modules/com/liferay/portal/ \  
&& cd $WILDFLY_HOME/modules/com/liferay/portal/ \  
# manually create else get error  
&& mkdir $WILDFLY_HOME/standalone/log  
&& mkdir $WILDFLY_HOME/standalone/data  
&& sha1sum $DOWNLOAD/liferay-ce-portal-dependencies-$LIFERAY_VERSION_FULL.zip
| grep $LIFERAY_DEPS_SHA1 \  
&& unzip $DOWNLOAD/liferay-ce-portal-dependencies-$LIFERAY_VERSION_FULL.zip >
/dev/null \  
&& mv liferay-ce-portal-dependencies-* main \  
&& cp /tmp/files/module.xml main/  
## CONFIGURATION  
RUN sed -i -e '/<paths/r /tmp/files/standalone-systemmodules.xml'
$LIFERAY_HOME/wildfly/modules/system/layers/base/sun/jdk/main/module.xml  
RUN sed -i '/org.jboss.as.weld/d' $WILDFLY_STANDALONE_CFG \  
&& sed -i -e '/\/extensions/r /tmp/files/standalone-systemproperties.xml'
$WILDFLY_STANDALONE_CFG \  
&& sed -i 's/<deployment-scanner/<deployment-scanner deployment-
timeout="360"/g' $WILDFLY_STANDALONE_CFG \  
&& sed -i -e '/<security-domains/r /tmp/files/standalone-securitydomain.xml'
$WILDFLY_STANDALONE_CFG \  
&& sed -i '/welcome-content/d' $WILDFLY_STANDALONE_CFG \  
&& sed -i '/urn:jboss:domain:weld/d' $WILDFLY_STANDALONE_CFG  
RUN cat /tmp/files/standalone.conf >> $WILDFLY_HOME/bin/standalone.conf  
  
## USER PERMISSIONS  
RUN chown -R jboss.users $LIFERAY_HOME  
  
## CLEANUP  
RUN rm -rf $HOME/files \  
&& rm -rf $DOWNLOAD  
  
# Expose the ports we're interested in EXPOSE 8080  
# Set the default command to run on boot  
# This will boot WildFly in the standalone mode and bind to all interface  
USER jboss  
CMD $WILDFLY_HOME/bin/standalone.sh -b 0.0.0.0  

