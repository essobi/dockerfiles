FROM mouflonjp/fiapd  
MAINTAINER mouflon-jp  
  
ENV PHP_BRIDGE_DIST_URL https://downloads.sourceforge.net/project/php-java-
bridge/Binary%20package  
ENV PHP_BRIDGE_FILE php-java-bridge_7.1.3/JavaBridgeTemplate713.war  
ENV PHP_BRIDGE_SHA512
0b1e36c0565d3f1f40bdd760fa98d70fb4f0f8f82a8129daf7f23e4ba3416d12f462c16cd90a2f35916fba9e761a0599d923e04c751cf572ad0c51265a50cbfa  
  
ENV JPGRAPH_DIST_URL https://fossies.org/linux/www/  
ENV JPGRAPH_VERSION 4.0.2  
ENV JPGRAPH_DIST_MD5 c691085c98cadbeb0a3bbebaca480852  
  
RUN apk update \  
&& apk --no-cache add php5 php5-cgi php5-soap php5-pgsql php5-gd \  
&& ln -s /usr/bin/php-cgi5 /usr/bin/php-cgi \  
&& ln -s /usr/bin/php5 /usr/bin/php \  
&& sed -i -e 's/display_errors = Off/display_errors = On/' /etc/php5/php.ini \  
&& cd /usr/local/tomcat/webapps/ \  
&& wget -O PHPBridge.war "${PHP_BRIDGE_DIST_URL}/${PHP_BRIDGE_FILE}" \  
&& echo "${PHP_BRIDGE_SHA512} *PHPBridge.war" | sha512sum -c - \  
&& mkdir PHPBridge \  
&& unzip -q PHPBridge.war -d PHPBridge \  
&& rm PHPBridge.war \  
&& cd /usr/local/tomcat/webapps/PHPBridge \  
&& wget -O FIAPStorage2.zip
"${FIAPSTORAGE_DIST_URL}/FIAPStorage2-${FIAPSTORAGE_VERSION}.zip" \  
&& echo "${FIAPSTORAGE_SHA512} *FIAPStorage2.zip" | sha512sum -c - \  
&& unzip -q FIAPStorage2.zip FIAPStorage2/var/www/* \  
&& mv ./FIAPStorage2/var/www/* . \  
&& rm -rf ./FIAPStorage2 \  
&& rm FIAPStorage2.zip \  
&& wget -O jpgraph.tar.gz
"${JPGRAPH_DIST_URL}/jpgraph-${JPGRAPH_VERSION}.tar.gz" \  
&& echo "${JPGRAPH_DIST_MD5} *jpgraph.tar.gz" | md5sum -c - \  
&& tar xz -f jpgraph.tar.gz -C ./WEB-INF/ \  
&& mv -f ./WEB-INF/jpgraph*/ ./WEB-INF/jpgraph/ \  
&& rm -rf ./WEB-INF/jpgraph/docs/ \  
&& rm jpgraph.tar.gz \  
&& sed -i -e
's|http://localhost/axis2/services/FIAPStorage?wsdl|http://localhost:8080/axis2/services/FIAPStorage?wsdl|'
index.php archive_view.php \  
&& sed -i -e "2i require_once('phpbridge.inc');\r" index.php \  
&& sed -i -e 's/dbname=fiapstorage2
user=postgres/host=".getenvj("POSTGRESQL_HOSTNAME")."
dbname=".getenvj("POSTGRESQL_DBNAME")." user=postgres/' index.php \  
&& sed -i -E
's|/usr/local/jpgraph-[0-9.]+/|/usr/local/tomcat/webapps/PHPBridge/WEB-
INF/jpgraph/|g' archive_view.php  
  
COPY changeContext.php /usr/local/tomcat/webapps/PHPBridge  
COPY phpbridge.inc /usr/local/tomcat/webapps/PHPBridge  
  
RUN /usr/bin/php5 /usr/local/tomcat/webapps/PHPBridge/changeContext.php \  
&& rm /usr/local/tomcat/webapps/PHPBridge/changeContext.php

