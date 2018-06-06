FROM openjdk:8-jre-alpine  
  
ENV CATALINA_HOME /usr/local/tomcat  
ENV PATH $CATALINA_HOME/bin:$PATH  
RUN mkdir -p "$CATALINA_HOME"  
WORKDIR $CATALINA_HOME  
  
# let "Tomcat Native" live somewhere isolated  
ENV TOMCAT_NATIVE_LIBDIR $CATALINA_HOME/native-jni-lib  
ENV LD_LIBRARY_PATH ${LD_LIBRARY_PATH:+$LD_LIBRARY_PATH:}$TOMCAT_NATIVE_LIBDIR  
  
RUN apk add --no-cache gnupg  
  
# see https://www.apache.org/dist/tomcat/tomcat-$TOMCAT_MAJOR/KEYS  
# see also "update.sh" (https://github.com/docker-
library/tomcat/blob/master/update.sh)  
ENV GPG_KEYS 05AB33110949707C93A279E3D3EFE6B686867BA6
07E48665A34DCAFAE522E5E6266191C37C037D42
47309207D818FFD8DCD3F83F1931D684307A10A5
541FBE7D8F78B25E055DDEE13C370389288584E7
61B832AC2F1C5A90F0F9B00A1C506407564C17A3
713DA88BE50911535FE716F5208B0AB1D63011C7
79F7026C690BAA50B92CD8B66A3AD3F4F22C4FED
9BA44C2621385CB966EBA586F72C284D731FABEE
A27677289986DB50844682F8ACB77FC2E86E29AC
A9C5DF4D22E99998D9875A5110C01C5A2F6059E7
DCFD35E0BF8CA7344752DE8B6FB21E8933C60243
F3A04C595DB5B6A5F1ECA43E3B7BBB100D811BBE
F7DA48BB64BCB84ECBA7EE6935CD23C10D498E23  
RUN set -ex; \  
for key in $GPG_KEYS; do \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key"; \  
done  
  
ENV TOMCAT_MAJOR 8  
ENV TOMCAT_VERSION 8.0.47  
#
https://issues.apache.org/jira/browse/INFRA-8753?focusedCommentId=14735394#comment-14735394  
ENV TOMCAT_TGZ_URL
https://www.apache.org/dyn/closer.cgi?action=download&filename=tomcat/tomcat-$TOMCAT_MAJOR/v$TOMCAT_VERSION/bin/apache-
tomcat-$TOMCAT_VERSION.tar.gz  
# not all the mirrors actually carry the .asc files :'(  
ENV TOMCAT_ASC_URL
https://www.apache.org/dist/tomcat/tomcat-$TOMCAT_MAJOR/v$TOMCAT_VERSION/bin/apache-
tomcat-$TOMCAT_VERSION.tar.gz.asc  
  
RUN set -x \  
\  
&& apk add --no-cache --virtual .fetch-deps \  
ca-certificates \  
tar \  
openssl \  
&& wget -O tomcat.tar.gz "$TOMCAT_TGZ_URL" \  
&& wget -O tomcat.tar.gz.asc "$TOMCAT_ASC_URL" \  
&& gpg --batch --verify tomcat.tar.gz.asc tomcat.tar.gz \  
&& tar -xvf tomcat.tar.gz --strip-components=1 \  
&& rm bin/*.bat \  
&& rm tomcat.tar.gz* \  
\  
&& nativeBuildDir="$(mktemp -d)" \  
&& tar -xvf bin/tomcat-native.tar.gz -C "$nativeBuildDir" \--strip-
components=1 \  
&& apk add --no-cache --virtual .native-build-deps \  
apr-dev \  
gcc \  
libc-dev \  
make \  
"openjdk${JAVA_VERSION%%[-~bu]*}"="$JAVA_ALPINE_VERSION" \  
openssl-dev \  
&& ( \  
export CATALINA_HOME="$PWD" \  
&& cd "$nativeBuildDir/native" \  
&& ./configure \  
\--libdir="$TOMCAT_NATIVE_LIBDIR" \  
\--prefix="$CATALINA_HOME" \  
\--with-apr="$(which apr-1-config)" \  
\--with-java-home="$(docker-java-home)" \  
\--with-ssl=yes \  
&& make -j$(getconf _NPROCESSORS_ONLN) \  
&& make install \  
) \  
&& runDeps="$( \  
scanelf --needed --nobanner --recursive "$TOMCAT_NATIVE_LIBDIR" \  
| awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \  
| sort -u \  
| xargs -r apk info --installed \  
| sort -u \  
)" \  
&& apk add --virtual .tomcat-native-rundeps $runDeps \  
&& apk del .fetch-deps .native-build-deps \  
&& rm -rf "$nativeBuildDir" \  
&& rm bin/tomcat-native.tar.gz  
  
# verify Tomcat Native is working properly  
RUN set -e \  
&& nativeLines="$(catalina.sh configtest 2>&1)" \  
&& nativeLines="$(echo "$nativeLines" | grep 'Apache Tomcat Native')" \  
&& nativeLines="$(echo "$nativeLines" | sort -u)" \  
&& if ! echo "$nativeLines" | grep 'INFO: Loaded APR based Apache Tomcat
Native library' >&2; then \  
echo >&2 "$nativeLines"; \  
exit 1; \  
fi  
  
# Change upload limit that is 50Megas in Tomcat 8  
RUN sed -i 's/52428800/104857600/' /usr/local/tomcat/webapps/manager/WEB-
INF/web.xml  
  
# Admin  
ENV PASS admin  
RUN sed -i 's/resourceName="UserDatabase"/resourceName="UserDatabase"
digest="sha1"/' /usr/local/tomcat/conf/server.xml \  
&& mv /usr/local/tomcat/conf/tomcat-users.xml /usr/local/tomcat/conf/tomcat-
users.xml.orig \  
&& mv /usr/local/tomcat/conf/context.xml
/usr/local/tomcat/conf/context.xml.orig  
  
# Connectors Java  
ENV URL_JDBC="https://github.com/luvres/jdbc/raw/master"  
ENV MYSQL_CONN_J_VERSION 5.1.44  
ENV MYSQL_CONN_J mysql-connector-java-$MYSQL_CONN_J_VERSION-bin.jar  
ENV MYSQL_CONN_J_URL $URL_JDBC/$MYSQL_CONN_J  
  
ENV MARIADB_CONN_J_VERSION 2.2.0  
ENV MARIADB_CONN_J mariadb-java-client-$MARIADB_CONN_J_VERSION.jar  
ENV MARIADB_CONN_J_URL $URL_JDBC/$MARIADB_CONN_J  
  
ENV POSTGRES_CONN_J postgresql-42.1.4.jar  
ENV POSTGRES_CONN_J_URL $URL_JDBC/$POSTGRES_CONN_J  
  
ENV ORACLE_CONN_J ojdbc6.jar  
ENV ORACLE_CONN_J_URL $URL_JDBC/$ORACLE_CONN_J  
  
RUN apk add --no-cache --virtual openssl \  
&& wget -c $MYSQL_CONN_J_URL -O /usr/local/tomcat/lib/$MYSQL_CONN_J \  
&& wget -c $MARIADB_CONN_J_URL -O /usr/local/tomcat/lib/$MARIADB_CONN_J \  
&& wget -c $POSTGRES_CONN_J_URL -O /usr/local/tomcat/lib/$POSTGRES_CONN_J \  
&& wget -c $ORACLE_CONN_J_URL -O /usr/local/tomcat/lib/$ORACLE_CONN_J \  
&& wget -c $URL_JDBC/probe.war -O /usr/local/tomcat/webapps/probe.war  
  
# Datasource  
ENV PORT_MYSQL 3306  
ENV USER_MYSQL root  
ENV PASS_MYSQL root  
ENV DB_MYSQL dbzone  
ENV HOST_MYSQL mysql-host  
ENV JNDI_MYSQL JNDI-MySQL  
  
ENV PORT_ORACLE 1521  
ENV USER_ORACLE system  
ENV PASS_ORACLE oracle  
ENV DB_ORACLE XE  
ENV HOST_ORACLE oracle-host  
ENV JNDI_ORACLE JNDI-Oracle  
  
ENV PORT_MARIADB 3306  
ENV USER_MARIADB root  
ENV PASS_MARIADB maria  
ENV DB_MARIADB dbzone  
ENV HOST_MARIADB mariadb-host  
ENV JNDI_MARIADB JNDI-MariaDB  
  
ENV PORT_POSTGRES 5432  
ENV USER_POSTGRES postgres  
ENV PASS_POSTGRES postgres  
ENV DB_POSTGRES postgres  
ENV HOST_POSTGRES postgres-host  
ENV JNDI_POSTGRES JNDI-PostgreSQL  
  
  
EXPOSE 8080  
ADD start.sh /etc/start.sh  
CMD ["sh", "/etc/start.sh"]  

