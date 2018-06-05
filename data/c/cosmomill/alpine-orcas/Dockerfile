FROM cosmomill/alpine-gradle  
  
MAINTAINER Rene Kanzler, me at renekanzler dot com  
  
# cosmomill/alpine-gradle changes the user to gradle but we need root  
USER root  
  
# add bash to make sure our scripts will run smoothly  
# cosmomill/alpine-gradle already added bash  
# grab curl to download installation files  
RUN apk --update add --no-cache curl ca-certificates  
  
# install bsdtar  
RUN apk --update add --no-cache libarchive-tools  
  
ONBUILD ARG ORACLE_INSTANTCLIENT_FILE  
ONBUILD ARG ORACLE_SQLPLUS_FILE  
ONBUILD ARG ORACLE_JDBC_FILE  
ONBUILD ARG ORACLE_JDBC12_FILE  
ONBUILD ARG APEX_FILE  
  
# install git  
RUN apk --update add --no-cache git  
  
# install apache ant  
ENV ANT_VERSION 1.10.1  
ENV ANT_DOWNLOAD_URL http://archive.apache.org/dist/ant/binaries/apache-
ant-$ANT_VERSION-bin.tar.gz  
ENV ANT_HOME /usr/share/ant  
ENV PATH $PATH:$ANT_HOME/bin  
  
# download and extract apache ant  
RUN curl -f#L $ANT_DOWNLOAD_URL | bsdtar -C /usr/share/ -xf- \  
&& ln -s /usr/share/apache-ant-$ANT_VERSION /usr/share/ant  
  
# install apache ant contrib  
ENV ANT_CONTRIB_VERSION 1.0b3  
ENV ANT_CONTRIB_DOWNLOAD_URL http://downloads.sourceforge.net/project/ant-
contrib/ant-contrib/$ANT_CONTRIB_VERSION/ant-contrib-$ANT_CONTRIB_VERSION-
bin.tar.gz  
  
# download and extract apache ant contrib  
RUN curl -f#L $ANT_CONTRIB_DOWNLOAD_URL | bsdtar --strip-components=1 -C
$ANT_HOME/lib -xf- ant-contrib/ant-contrib-1.0b3.jar  
  
# install Oracle Instant Client  
ENV ORACLE_INSTANTCLIENT_MAJOR 12_2  
ENV ORACLE_INSTANTCLIENT_VERSION 12.2.0.1.0  
ENV ORACLE_HOME /usr/local/lib/instantclient  
ENV PATH $PATH:$ORACLE_HOME  
  
# install Oracle Instant Client prerequisites  
RUN apk --update add --no-cache libaio  
  
# download and extract Oracle Instant Client  
ONBUILD ADD $ORACLE_INSTANTCLIENT_FILE /tmp/  
ONBUILD ADD $ORACLE_SQLPLUS_FILE /tmp/  
ONBUILD ADD $ORACLE_JDBC_FILE /tmp/  
  
ONBUILD RUN bsdtar -C /usr/local/lib -xf /tmp/instantclient-basic-
linux.x64-$ORACLE_INSTANTCLIENT_VERSION.zip \  
&& bsdtar -C /usr/local/lib -xf /tmp/instantclient-sqlplus-
linux.x64-$ORACLE_INSTANTCLIENT_VERSION.zip \  
&& bsdtar -C /usr/local/lib -xf /tmp/instantclient-jdbc-
linux.x64-$ORACLE_INSTANTCLIENT_VERSION.zip \  
\  
&& chown -R root:root /usr/local/lib/instantclient_$ORACLE_INSTANTCLIENT_MAJOR
\  
&& find /usr/local/lib/instantclient_$ORACLE_INSTANTCLIENT_MAJOR -type f -exec
chmod 644 {} \; \  
&& chmod 755 /usr/local/lib/instantclient_$ORACLE_INSTANTCLIENT_MAJOR/adrci \  
&& chmod 755 /usr/local/lib/instantclient_$ORACLE_INSTANTCLIENT_MAJOR/genezi \  
&& chmod 755 /usr/local/lib/instantclient_$ORACLE_INSTANTCLIENT_MAJOR/uidrvci
\  
&& chmod 755 /usr/local/lib/instantclient_$ORACLE_INSTANTCLIENT_MAJOR/sqlplus
\  
&& ln -s /usr/local/lib/instantclient_$ORACLE_INSTANTCLIENT_MAJOR $ORACLE_HOME
\  
\  
&& rm -f /tmp/instantclient-basic-linux.x64-$ORACLE_INSTANTCLIENT_VERSION.zip
\  
&& rm -f /tmp/instantclient-sqlplus-
linux.x64-$ORACLE_INSTANTCLIENT_VERSION.zip \  
&& rm -f /tmp/instantclient-jdbc-linux.x64-$ORACLE_INSTANTCLIENT_VERSION.zip \  
\  
&& echo $ORACLE_HOME >> /usr/glibc-compat/etc/ld.so.conf \  
&& /usr/glibc-compat/sbin/ldconfig  
  
# install Orcas  
ENV APEX_VERSION 5.1.1  
ENV APEX_HOME /opt/apex  
ENV ORCAS_GIT_REPOSITORY https://github.com/opitzconsulting/orcas.git  
  
# pull Orcas  
RUN git clone \--progress --verbose --recursive "$ORCAS_GIT_REPOSITORY"
/opt/orcas/  
  
# add classes12.jar, needed by Oracle XE  
ONBUILD ADD $ORACLE_JDBC12_FILE /tmp/  
  
ONBUILD RUN mkdir -p $ORACLE_HOME/oui/jlib \  
&& mv /tmp/classes12.jar $ORACLE_HOME/oui/jlib/ \  
&& chmod 644 $ORACLE_HOME/oui/jlib/classes12.jar \  
&& rm -f /tmp/classes12.jar  
  
# download and extract APEX 5  
ONBUILD ADD $APEX_FILE /tmp/  
  
ONBUILD RUN mkdir -p /opt/apex \  
&& bsdtar --strip-components=1 -C /opt/apex -xf /tmp/apex_$APEX_VERSION.zip \  
&& chmod 755 /opt/apex \  
&& find /opt/apex -type d -exec chmod 755 {} \; \  
&& rm -f /tmp/apex_$APEX_VERSION.zip  
  
# define mountable directories  
ONBUILD VOLUME /home  
  
ENV ORCAS_HOME /home/orcas  
ENV DATABASE_HOSTNAME localhost  
ENV DATABASE_SID XE  
ENV DATABASE_PORT 1521  
ENV SCHEMA SCOTT  
ENV SCHEMA_USERNAME SCOTT  
ENV SCHEMA_PASSWORD TIGER  
  
COPY docker-entrypoint.sh /usr/local/bin/  
RUN chmod 755 /usr/local/bin/docker-entrypoint.sh  
ENTRYPOINT ["docker-entrypoint.sh"]  

