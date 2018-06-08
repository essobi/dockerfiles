FROM tomcat:9.0.0-jre8-alpine  
MAINTAINER mouflon-jp  
  
ENV FIAPSTORAGE_DIST_URL http://fiap-dev.gutp.ic.i.u-tokyo.ac.jp/dist  
ENV FIAPSTORAGE_VERSION 20170406  
ENV FIAPSTORAGE_SHA512
f4b262f469f082d54a4de5b96d545a74f780f4bec54fffcf42f3c650ec5cd2e2c8a25e7565da4d9b0deb00e5f349f46d188664f9a7f957fc23c66670428066fc  
  
ENV CATALINA_BASE /usr/local/tomcat  
  
ENV AXIS2_DIST_URL http://www-us.apache.org/dist/axis/axis2/java/core/  
ENV AXIS2_VERSION 1.7.5  
ENV AXIS2_WAR_SHA1 1d20e3e1f413ce413de8f1fb3d7a1c3f312f5a55  
  
ENV POSTGRESQL_HOSTNAME fiapd-db  
ENV POSTGRESQL_DBNAME fiapstorage2  
ENV POSTGRESQL_CONNECTION_STRING
jdbc:postgresql://${POSTGRESQL_HOSTNAME}/${POSTGRESQL_DBNAME}  
  
ENV POSTGRESQL_JDBC_DRIVER_DIST_URL https://jdbc.postgresql.org/download/  
ENV POSTGRESQL_JDBC_DRIVER_VERSION 42.1.1  
ENV POSTGRESQL_JDBC_DRIVER_SHA512
2894a045ce9a4870c97d3c4c7395468f17b47669bf10b5ff53dc79c06ab5a2b8c3bd4d3331ca3c83dd83a4a977dfc26ade16fbbe290d494565fad50b65dd0ae1  
  
RUN apk update \  
&& apk --no-cache add openssl \  
&& cd /usr/local/tomcat \  
&& wget -O FIAPStorage2.zip
"${FIAPSTORAGE_DIST_URL}/FIAPStorage2-${FIAPSTORAGE_VERSION}.zip" \  
&& echo "${FIAPSTORAGE_SHA512} *FIAPStorage2.zip" | sha512sum -c - \  
&& unzip -q FIAPStorage2.zip \  
&& rm FIAPStorage2.zip \  
&& cd /usr/local/tomcat/webapps/ \  
&& wget -O axis2-war.zip
"${AXIS2_DIST_URL}/${AXIS2_VERSION}/axis2-${AXIS2_VERSION}-war.zip" \  
&& echo "${AXIS2_WAR_SHA1} *axis2-war.zip" | sha1sum -c - \  
&& mkdir axis2 \  
&& unzip -q axis2-war.zip axis2.war \  
&& unzip -q axis2.war -d axis2 \  
&& rm axis2.war \  
&& rm axis2-war.zip \  
&& wget -O postgresql.jar
"${POSTGRESQL_JDBC_DRIVER_DIST_URL}/postgresql-${POSTGRESQL_JDBC_DRIVER_VERSION}.jar"
\  
&& echo "${POSTGRESQL_JDBC_DRIVER_SHA512} *postgresql.jar" | sha512sum -c - \  
&& mv postgresql.jar /usr/local/tomcat/webapps/axis2/WEB-INF/lib/ \  
&& cp "/usr/local/tomcat/FIAPStorage2/FIAPStorage2-${FIAPSTORAGE_VERSION}.aar"
/usr/local/tomcat/webapps/axis2/WEB-INF/services/FIAPStorage2.aar \  
&& cd /usr/local/tomcat \  
&& mkdir -p /usr/local/storage2/log \  
&& mkdir -p /usr/local/tomcat/webapps/axis2/WEB-INF/conf/storage2 \  
&& keytool -genkey -noprompt -alias tomcat -keyalg RSA -keystore
/usr/local/tomcat/conf/localhost-rsa.jks -dname "CN=localhost, OU=Unknown,
O=Unknown, L=Unknown, S=Unknown, C=Unknown" -storepass changeit -keypass
changeit \  
&& rm -rf /usr/local/tomcat/FIAPStorage2  
  
COPY server.xml /usr/local/tomcat/conf/  
COPY storage2.xml /usr/local/tomcat/webapps/axis2/WEB-INF/conf/storage2/  
COPY axis2.xml /usr/local/tomcat/webapps/axis2/WEB-INF/conf/  
  
WORKDIR /usr/local/tomcat/  
EXPOSE 8080 8443  
CMD ["catalina.sh", "run"]

