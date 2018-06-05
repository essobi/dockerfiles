FROM keensoft/alfresco-docker-template:201702-GA  
MAINTAINER keensoft.es  
  
RUN set -x \  
&& yum update -y \  
&& yum clean all  
  
ENV ALF_HOME /usr/local/alfresco  
ENV CATALINA_HOME /usr/local/alfresco/tomcat  
WORKDIR $ALF_HOME  
  
# basic configuration  
RUN set -x \  
&& ln -s /usr/local/tomcat /usr/local/alfresco/tomcat \  
&& mkdir -p $CATALINA_HOME/conf/Catalina/localhost
$CATALINA_HOME/shared/classes/alfresco/web-extensio $CATALINA_HOME/shared/lib
$ALF_HOME/modules/share \  
&& mv $DIST/web-server/conf/Catalina/localhost/share.xml
tomcat/conf/Catalina/localhost \  
&& mv $DIST/web-server/webapps/share.war tomcat/webapps/ \  
&& mv $DIST/bin . \  
&& mv $DIST/amps_share . \  
&& mv $DIST/licenses . \  
&& mv $DIST/README.txt . \  
&& rm -rf $CATALINA_HOME/webapps/docs \  
&& rm -rf $CATALINA_HOME/webapps/examples \  
&& rm -rf $DIST \  
&& curl -s https://letsencrypt.org/certs/lets-encrypt-x1-cross-signed.pem -o
/lets-encrypt-x1-cross-signed.pem \  
&& curl -s https://letsencrypt.org/certs/lets-encrypt-x2-cross-signed.pem -o
/lets-encrypt-x2-cross-signed.pem \  
&& curl -s https://letsencrypt.org/certs/lets-encrypt-x3-cross-signed.pem -o
/lets-encrypt-x3-cross-signed.pem \  
&& curl -s https://letsencrypt.org/certs/lets-encrypt-x4-cross-signed.pem -o
/lets-encrypt-x4-cross-signed.pem \  
&& keytool -trustcacerts -keystore $JAVA_HOME/jre/lib/security/cacerts
-storepass changeit -noprompt -importcert -alias lets-encrypt-x1-cross-signed
-file /lets-encrypt-x1-cross-signed.pem \  
&& keytool -trustcacerts -keystore $JAVA_HOME/jre/lib/security/cacerts
-storepass changeit -noprompt -importcert -alias lets-encrypt-x2-cross-signed
-file /lets-encrypt-x2-cross-signed.pem \  
&& keytool -trustcacerts -keystore $JAVA_HOME/jre/lib/security/cacerts
-storepass changeit -noprompt -importcert -alias lets-encrypt-x3-cross-signed
-file /lets-encrypt-x3-cross-signed.pem \  
&& keytool -trustcacerts -keystore $JAVA_HOME/jre/lib/security/cacerts
-storepass changeit -noprompt -importcert -alias lets-encrypt-x4-cross-signed
-file /lets-encrypt-x4-cross-signed.pem \  
&& rm -f /*.pem  
  
COPY assets/tomcat/catalina.properties tomcat/conf/catalina.properties  
COPY assets/tomcat/setenv.sh tomcat/bin/setenv.sh  
COPY assets/share/share-config-custom.xml tomcat/shared/classes/alfresco/web-
extension/share-config-custom.xml  
  
# AMPS installation  
COPY assets/share/apply_share_amps.sh $ALF_HOME/bin/apply_amps.sh  
COPY assets/amps_share amps_share  
RUN set -x \  
&& wget
https://downloads.loftux.net/public/content/org/alfresco/integrations/alfresco-
googledocs-share/3.0.3/alfresco-googledocs-share-3.0.3.amp -O
/usr/local/alfresco/amps_share/alfresco-googledocs-share.amp  
RUN bash ./bin/apply_amps.sh -force -nobackup  
  
ENV PATH $ALF_HOME/bin:$PATH  
ENV LANG en_GB.utf8  
  
RUN useradd -ms /bin/bash alfresco  
RUN set -x && chown -RL alfresco:alfresco $ALF_HOME  
USER alfresco  
  
EXPOSE 8080 8009  
CMD ["catalina.sh", "run"]  

