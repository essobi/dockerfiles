FROM thomasbjackson/java:oracle-java8  
  
MAINTAINER Tom Jackson thomas.jackson@nordstrom.com  
  
# ENV http_proxy http://pbcld-proxy.nordstrom.net:3128  
# ENV https_proxy https://pbcld-proxy.nordstrom.net:3128  
# ENV no_proxy localhost,10.0.0/8,nordstrom.net  
# Version of Confluence to run  
# The only change need to run a different version is a change to this variable  
ENV CONFLUENCE_VERSION 5.8.14  
# MYSQL Version  
ENV MYSQL_VERSION 5.1.37  
# Atlassian's download site for Confluence  
ENV DOWNLOAD_URL
https://downloads.atlassian.com/software/confluence/downloads/atlassian-
confluence-  
  
# Oracle's MySQL download site  
ENV MYSQL_DOWNLOAD_URL http://cdn.mysql.com/Downloads/Connector-J/mysql-
connector-java-  
  
# Confluence install and home paths  
ENV CONFLUENCE_HOME /var/local/atlassian/confluence  
ENV CONFLUENCE_INSTALL /usr/local/confluence  
  
# Install xmlstarlet for use in manipulating xml files in situ  
RUN set -x \  
&& apt-get update --quiet \  
&& apt-get install --quiet --yes --no-install-recommends libtcnative-1
xmlstarlet  
  
# Install VIM so we have at least some editing capability  
RUN apt-get install vim -y  
  
# Install zip/unzip for troubleshooting purposes (creating and copying
archives to/from server)  
# and curl for download stuff  
RUN apt-get install zip -y  
RUN apt-get install unzip -y  
RUN apt-get install curl -y  
  
# Install posgres client for troubleshooting DB issues  
RUN apt-get install postgresql-client -y  
  
# Create the install and home directories, setup ownership to daemon:daemon  
# then download and expand Confluence binaries into the install dir.  
RUN mkdir -p "${CONFLUENCE_HOME}" \  
&& mkdir -p "${CONFLUENCE_INSTALL}" \  
&& chown daemon:daemon "${CONFLUENCE_HOME}" \  
&& chown daemon:daemon "${CONFLUENCE_INSTALL}" \  
&& curl -L --silent ${DOWNLOAD_URL}${CONFLUENCE_VERSION}.tar.gz | tar -xz
--strip=1 -C "${CONFLUENCE_INSTALL}" \--no-same-owner \  
&& chmod -R 770 "${CONFLUENCE_INSTALL}/conf" \  
&& chmod -R 770 "${CONFLUENCE_INSTALL}/temp" \  
&& chmod -R 770 "${CONFLUENCE_INSTALL}/logs" \  
&& chmod -R 770 "${CONFLUENCE_INSTALL}/work" \  
&& chown -R daemon:daemon "${CONFLUENCE_INSTALL}/conf" \  
&& chown -R daemon:daemon "${CONFLUENCE_INSTALL}/temp" \  
&& chown -R daemon:daemon "${CONFLUENCE_INSTALL}/logs" \  
&& chown -R daemon:daemon "${CONFLUENCE_INSTALL}/work"  
# Add the MySQL driver  
RUN curl -L --silent ${MYSQL_DOWNLOAD_URL}${MYSQL_VERSION}.tar.gz | tar -xz
--strip=1 -C "${CONFLUENCE_INSTALL}/confluence/WEB-INF/lib" \--no-same-owner  
  
# point Confluence to its home directory.  
RUN echo "confluence.home=${CONFLUENCE_HOME}" >
${CONFLUENCE_INSTALL}/confluence/WEB-INF/classes/confluence-init.properties  
  
# Set default env variables used in urlrewrite rules  
# These can be overridden via docker run -e arguments to suit your FQDN  
ENV TL_DOMAIN net  
ENV SL_DOMAIN nordstrom  
ENV CNAME confluence  
  
# add the urlrewrite file that includes http-to-https rewrites  
ADD configs/urlrewrite.xml $CONFLUENCE_INSTALL/confluence/WEB-
INF/urlrewrite.xml  
  
# update web.xml to increase session timeout to 8 hours  
RUN xmlstarlet ed --inplace -N my=http://java.sun.com/xml/ns/j2ee \  
-u "/my:web-app/my:session-config/my:session-timeout" -v 480 \   
$CONFLUENCE_INSTALL/confluence/WEB-INF/web.xml  
  
# update web.xml to set the url-pattern to enable http-to-https re-writes  
# (the default setting blocks re-writes)  
RUN xmlstarlet ed --inplace -N my=http://java.sun.com/xml/ns/j2ee -u \  
"/my:web-app/my:filter-mapping/my:filter-
name[text()='UrlRewriteFilter']/../my:url-pattern[text()='/s/*']" \  
-v '/*' $CONFLUENCE_INSTALL/confluence/WEB-INF/web.xml   
  
# configure Confluence for use behind an ELB by adding proxy-related
attributes to server.xml  
RUN xmlstarlet ed --inplace --insert "/Server/Service/Connector" \--type attr
-n scheme -v https $CONFLUENCE_INSTALL/conf/server.xml  
RUN xmlstarlet ed --inplace --insert "/Server/Service/Connector" \--type attr
-n proxyPort -v 443 $CONFLUENCE_INSTALL/conf/server.xml  
RUN xmlstarlet ed --inplace --insert "/Server/Service/Connector" \--type attr
-n secure -v true $CONFLUENCE_INSTALL/conf/server.xml  
  
# Adding Connector for ELB health check on port 8091 to server.xml  
# Because health checks look the HTTP 200, key is for this connector to NOT
redirect  
# requests anywhere  
RUN xmlstarlet ed --inplace -P -S -L -s /Server/Service -t elem -n
ConnectorTMP -v "" \  
-i //ConnectorTMP -t attr -n "port" -v "8091" \   
-i //ConnectorTMP -t attr -n "protocol" -v "HTTP/1.1" \   
-i //ConnectorTMP -t attr -n "connectionTimeout" -v "20000" \   
-i //ConnectorTMP -t attr -n "redirectPort" -v "8444" \   
-r //ConnectorTMP -v Connector \   
$CONFLUENCE_INSTALL/conf/server.xml  
  
# remove any default JAVA_OPTS settings from setenv.sh. JAVA_OPTS defaults are
set via pipeline script.  
RUN sed -i '/JAVA_OPTS/d' $CONFLUENCE_INSTALL/bin/setenv.sh  
  
# Add the start-up script and make it executable by root  
ADD configs/docker-startup.sh ${CONFLUENCE_INSTALL}/bin/docker-startup.sh  
RUN chmod 0554 ${CONFLUENCE_INSTALL}/bin/docker-startup.sh  
  
# HTTP Ports (one standard, the second for ELB health checks)  
EXPOSE 8090 8091  
# Set the working directory to the directory where confluence will be launched  
WORKDIR $CONFLUENCE_INSTALL  
  
# Run startup script  
CMD ["./bin/docker-startup.sh"]

