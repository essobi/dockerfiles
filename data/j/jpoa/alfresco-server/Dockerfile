FROM keensoft/alfresco-docker-template:201702-GA  
MAINTAINER keensoft.es  
  
RUN set -x \  
&& yum install -y \  
ImageMagick \  
ghostscript \  
&& yum clean all  
  
ENV ALF_HOME /usr/local/alfresco  
ENV CATALINA_HOME /usr/local/alfresco/tomcat  
WORKDIR $ALF_HOME  
  
# basic configuration  
RUN set -x \  
&& ln -s /usr/local/tomcat /usr/local/alfresco/tomcat \  
&& mkdir -p $CATALINA_HOME/conf/Catalina/localhost
$CATALINA_HOME/shared/classes/alfresco/extension $CATALINA_HOME/shared/lib
$ALF_HOME/modules/platform \  
&& mv $DIST/web-server/conf/Catalina/localhost/alfresco.xml
tomcat/conf/Catalina/localhost/ \  
&& mv $DIST/web-server/lib/*.jar tomcat/lib/ \  
&& mv $DIST/web-server/webapps/alfresco.war tomcat/webapps/ \  
&& mv $DIST/alf_data . \  
&& mv $DIST/amps . \  
&& mv $DIST/bin . \  
&& mv $DIST/licenses . \  
&& mv $DIST/README.txt . \  
&& rm -rf $CATALINA_HOME/webapps/docs \  
&& rm -rf $CATALINA_HOME/webapps/examples \  
&& rm -rf $DIST  
  
COPY assets/tomcat/catalina.properties tomcat/conf/catalina.properties  
COPY assets/tomcat/setenv.sh tomcat/bin/setenv.sh  
COPY assets/alfresco/alfresco-global.properties
tomcat/shared/classes/alfresco-global.properties  
  
# AMPS installation  
COPY assets/alfresco/apply_alfresco_amps.sh $ALF_HOME/bin/apply_amps.sh  
COPY assets/amps amps  
# Download vti amp  
RUN set -x \  
&& wget
https://artifacts.alfresco.com/nexus/content/repositories/public/org/alfresco/integrations/alfresco-
googledocs-repo/3.0.4/alfresco-googledocs-repo-3.0.4.amp -O
/usr/local/alfresco/amps/alfresco-googledocs-repo.amp \  
&& wget
https://artifacts.alfresco.com/nexus/content/repositories/public/org/alfresco/aos-
module/alfresco-aos-module/1.1.6/alfresco-aos-module-1.1.6.amp -O
/usr/local/alfresco/amps/alfresco-aos-module.amp  
# && wget
https://downloads.loftux.net/public/content/org/alfresco/integrations/alfresco-
googledocs-share/3.0.3/alfresco-googledocs-share-3.0.3.amp -O
/usr/local/alfresco/amps/alfresco-googledocs-share.amp  
RUN bash ./bin/apply_amps.sh -nobackup  
  
# Add api-explorer WAR file  
RUN set -x \  
&& wget
https://artifacts.alfresco.com/nexus/service/local/repositories/releases/content/org/alfresco/api-
explorer/5.2.0/api-explorer-5.2.0.war -O tomcat/webapps/api-explorer.war  
#&& wget
https://artifacts.alfresco.com/nexus/service/local/repositories/releases/content/org/alfresco/aos-
module/alfresco-vti-bin/1.1.5/alfresco-vti-bin-1.1.5.war -O
tomcat/webapps/alfresco-vti-bin.war  
#&& wget https://downloads.loftux.net/public/content/org/alfresco/alfresco-
server-root/5.2.f/alfresco-server-root-5.2.f.war -O tomcat/webapps/root.war  
ENV PATH $ALF_HOME/bin:$PATH  
ENV LANG en_GB.utf8  
  
RUN useradd -ms /bin/bash alfresco  
RUN set -x && chown -RL alfresco:alfresco $ALF_HOME  
USER alfresco  
  
ENV JPDA_ADDRESS="9999"  
ENV JPDA_TRANSPORT="dt_socket"  
EXPOSE 8080 8009 9999  
VOLUME $ALF_HOME/alf_data  
CMD ["catalina.sh", "jpda", "run"]  

