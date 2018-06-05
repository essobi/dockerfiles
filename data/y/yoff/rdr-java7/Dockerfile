FROM yoff/rdr  
ENV ADDON_SCRIPT="/bootstrap/rdr-java7.sh"  
# Escalate out from limited user "ahsay"  
USER root  
  
  
# Copy in CBS files (tomcat, java, web.xml, etc)  
COPY cbs/ /cbs-temp  
  
  
# 'bootstrap' contains an addon (obsr-tls.sh), templates, and default certs  
COPY bootstrap/ /bootstrap  
  
  
# Change ownership  
RUN chown -R ${UID}:${GID} /cbs-temp /bootstrap  
  
  
# De-escalate from root  
USER ahsay  
  
  
RUN \  
#  
#  
# Create new library folder  
mkdir "${APP_HOME}/lib" && \  
#  
#  
# Move libraries from ${APP} and CBS  
mv \  
##  
##  
## Ahsay ANI (in v7 this file is moved inside cbs.jar)  
${APP_HOME}/tomcat/lib/ani.jar \  
##  
##  
## Bouncy Castle Provider  
${APP_HOME}/tomcat/lib/bcprov-jdk14-140.jar \  
## /cbs-temp/lib/bcprov-jdk15on-151.jar \  
##  
##  
## Commons (apache)  
${APP_HOME}/tomcat/lib/commons-beanutils.jar \  
${APP_HOME}/tomcat/lib/commons-collections.jar \  
${APP_HOME}/tomcat/lib/commons-digester.jar \  
${APP_HOME}/tomcat/lib/commons-fileupload.jar \  
${APP_HOME}/tomcat/lib/commons-lang.jar \  
${APP_HOME}/tomcat/lib/commons-logging.jar \  
${APP_HOME}/tomcat/lib/commons-validator.jar \  
## /cbs-temp/lib/commons-beanutils-1.8.0.jar \  
## /cbs-temp/lib/commons-chain-1.2.jar \  
## /cbs-temp/lib/commons-collections.jar \  
## /cbs-temp/lib/commons-digester-1.8.jar \  
## /cbs-temp/lib/commons-fileupload-1.1.1.jar \  
## /cbs-temp/lib/commons-io-1.1.jar \  
## /cbs-temp/lib/commons-io-2.5.jar \  
## /cbs-temp/lib/commons-lang.jar \  
## /cbs-temp/lib/commons-logging-1.1.3.jar \  
## /cbs-temp/lib/commons-validator-1.3.1.jar \  
##  
##  
## Java DOM - for XML manipulation  
${APP_HOME}/tomcat/lib/jdom.jar \  
## /cbs-temp/lib/jdom-1.1.3.jar \  
##  
##  
## Linux 64-bit shared object files  
# ${APP_HOME}/tomcat/lib/libNixUtilLinX64.so \  
${APP_HOME}/tomcat/lib/libFileSysUtilLinX64.so \  
## /cbs-temp/lib/LinX64/libFileSysUtilLinX64.so \  
## /cbs-temp/lib/LinX64/libNixUtilLinX64.so \  
##  
##  
## APR shared object (for OpenSSL in tomcat)  
/cbs-temp/lib/LinX64/libapr-1.so.0 \  
/cbs-temp/lib/LinX64/libcrypto.so.1.0.0 \  
/cbs-temp/lib/LinX64/libssl.so.1.0.0 \  
/cbs-temp/lib/LinX64/libtcnative-1.so \  
##  
##  
## Mail handler (for sending to SMTP)  
${APP_HOME}/tomcat/lib/mail.jar \  
## /cbs-temp/lib/javax.mail.jar \  
##  
##  
## Apache Struts  
${APP_HOME}/tomcat/lib/struts.jar \  
## /cbs-temp/lib/struts-core-1.3.10.jar \  
## /cbs-temp/lib/struts-tiles-1.3.10.jar \  
## /cbs-temp/lib/struts-extras-1.3.10.jar \  
## /cbs-temp/lib/struts-taglib-1.3.10.jar \  
##  
##  
## Destination library folder  
${APP_HOME}/lib/ && \  
#  
#  
# DELETE v6 tomcat and java  
rm -rf ${APP_HOME}/tomcat \  
${APP_HOME}/java-linux-x64 && \  
#  
#  
# Relocate java and tomcat from CBS  
mv /cbs-temp/tomcat ${APP_HOME} && \  
mv /cbs-temp/java-linux-x64 ${APP_HOME} && \  
#  
#  
# Tweak startup.sh: include new library folder, set LD_LIBRARY_PATH  
sed \  
-i ${APP_HOME}/bin/startup.sh \  
-e 's|JAVA_JNI_OPTS="-Djava.library.path=$CATALINA_HOME/lib"|JAVA_JNI_OPTS="-Djava.library.path=$CATALINA_HOME/lib:${APP_HOME}/lib"|g' \  
-e '/catalina.sh/i LD_LIBRARY_PATH="${APP_HOME}/lib"\nexport LD_LIBRARY_PATH' && \  
#  
#  
# Move Tomcat 7 default servlet and ssl certs from CBS  
mv \  
/cbs-temp/conf/web.xml \  
/cbs-temp/conf/ca.crt \  
/cbs-temp/conf/ssl.crt \  
/cbs-temp/conf/ssl.key \  
${APP_HOME}/conf/  

