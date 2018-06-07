FROM tomcat:8.5-jre8-alpine  
  
MAINTAINER Rene Kanzler, me at renekanzler dot com  
  
# add bash to make sure our scripts will run smoothly  
RUN apk --update add --no-cache bash  
  
# grab curl to download installation files  
RUN apk --update add --no-cache curl ca-certificates  
  
# install bsdtar  
RUN apk --update add --no-cache libarchive-tools  
  
# install some basic fonts for JasperReports Server  
RUN apk --update add --no-cache ttf-dejavu  
  
# install ncurses cause SQLcl needs tput  
RUN apk --update add --no-cache ncurses  
  
ONBUILD ARG ORACLE_JDBC_DRIVER  
ONBUILD ARG SQLCL_FILE  
  
ENV TZ GMT  
ENV TOMCAT_HOME /usr/local/tomcat  
ENV CATALINA_OPTS -Doracle.jdbc.defaultNChar=true -Xms1024m -Xmx2048m
-XX:PermSize=32m -XX:MaxPermSize=512m -Xss2m -XX:+UseConcMarkSweepGC
-XX:+CMSClassUnloadingEnabled  
ENV ORACLE_BASE /u01/app/oracle  
ENV ORACLE_HOME /u01/app/oracle/product/11.2.0/xe  
ENV ORACLE_SID XE  
ENV DATABASE_PORT 1521  
RUN mkdir /docker-entrypoint-import.d  
  
# download and extract JasperReports Server  
ENV JASPERSERVER_VERSION 7.1.0  
ENV JASPERSERVER_DOWNLOAD_URL
http://downloads.sourceforge.net/project/jasperserver/JasperServer/JasperReports%20Server%20Community%20Edition%20${JASPERSERVER_VERSION}/TIB_js-
jrs-cp_${JASPERSERVER_VERSION}_bin.zip  
ENV JASPERSERVER_BUILDOMATIC_DIR /usr/src/jasperserver/buildomatic  
  
RUN mkdir /usr/src \  
&& curl -f#L $JASPERSERVER_DOWNLOAD_URL | bsdtar -C /usr/src -xf- \  
&& mv /usr/src/jasperreports-server-cp-$JASPERSERVER_VERSION-bin
/usr/src/jasperserver \  
\  
# prepare JasperReports Server CE to use Oracle as repository database  
&& mkdir -p $JASPERSERVER_BUILDOMATIC_DIR/conf_source/db/oracle/jdbc \  
&& mkdir $JASPERSERVER_BUILDOMATIC_DIR/install_resources/sql/oracle \  
&& cp $JASPERSERVER_BUILDOMATIC_DIR/install_resources/export/js-catalog-mysql-
minimal-ce.zip $JASPERSERVER_BUILDOMATIC_DIR/install_resources/export/js-
catalog-oracle-minimal-ce.zip  
  
# grab some Oracle configuration files from JasperReports Server 5.6.0  
ENV JASPERSERVER5_DOWNLOAD_URL
http://downloads.sourceforge.net/project/jasperserver/JasperServer/JasperReports%20Server%20Community%20Edition%205.6.0/jasperreports-
server-cp-5.6.0-bin.zip  
  
RUN curl -f#L $JASPERSERVER5_DOWNLOAD_URL | bsdtar -C /tmp -xf- jasperreports-
server-cp-5.6.0-bin/buildomatic/conf_source/db/oracle/* jasperreports-server-
cp-5.6.0-bin/buildomatic/install_resources/sql/oracle/killSession.sql
jasperreports-server-
cp-5.6.0-bin/buildomatic/install_resources/sql/oracle/quartz.ddl \  
\  
# run bash to use brace expansion  
&& /bin/bash -c "mv /tmp/jasperreports-server-
cp-5.6.0-bin/buildomatic/conf_source/db/oracle/{db.properties,db.xml,db.template.properties,scripts.properties}
$JASPERSERVER_BUILDOMATIC_DIR/conf_source/db/oracle/ \  
&& mv /tmp/jasperreports-server-
cp-5.6.0-bin/buildomatic/install_resources/sql/oracle/{killSession.sql,quartz.ddl}
$JASPERSERVER_BUILDOMATIC_DIR/install_resources/sql/oracle/" \  
\  
&& rm -rf /tmp/*  
  
ONBUILD ADD $ORACLE_JDBC_DRIVER
$JASPERSERVER_BUILDOMATIC_DIR/conf_source/db/oracle/jdbc/  
ONBUILD ADD $ORACLE_JDBC_DRIVER $TOMCAT_HOME/lib/  
  
# set permissions  
RUN chmod 755 /usr/src/jasperserver \  
&& find /usr/src/jasperserver/ -type f -exec chmod 644 {} \; \  
&& find /usr/src/jasperserver/ -type d -exec chmod 755 {} \; \  
&& find /usr/src/jasperserver/ -name *.sh -type f -exec chmod 755 {} \; \  
&& chmod 755 /usr/src/jasperserver/apache-ant/bin/ant \  
&& chmod 755 $JASPERSERVER_BUILDOMATIC_DIR/js-ant  
  
ENV SQLCL_VERSION 18.1.1  
# install SQLcl  
ONBUILD ADD $SQLCL_FILE /tmp/  
ONBUILD RUN bsdtar -C /var/lib -xf /tmp/sqlcl-$SQLCL_VERSION.zip \  
&& ln -s /var/lib/sqlcl/bin/sql /usr/local/bin/sqlcl \  
&& rm -f /tmp/sqlcl-$SQLCL_VERSION.zip  
  
# define mountable directories  
VOLUME /usr/src/jasperserver $TOMCAT_HOME/webapps  
  
COPY wait-for-oracle.sh /usr/local/bin/  
RUN chmod 755 /usr/local/bin/wait-for-oracle.sh  
  
COPY docker-entrypoint.sh /usr/local/bin/  
RUN chmod 755 /usr/local/bin/docker-entrypoint.sh  
ENTRYPOINT ["docker-entrypoint.sh"]  
  
EXPOSE 8080  
CMD ["run"]  

