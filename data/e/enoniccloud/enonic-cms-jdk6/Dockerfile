FROM enoniccloud/java6  
  
MAINTAINER Erik Kaareng-Sunde <esu@enonic.com>  
  
#  
# Based on the official tomcat images, but with Oracle JDK 7 as java version
and som minor tweaks for Enonic CMS  
#  
ENV CATALINA_OPTS "-XX:MaxPermSize=256m -Xms2048m -Xmx2048m"  
ENV CMS_HOME /cms.home  
  
ENV CATALINA_HOME /usr/local/tomcat  
ENV PATH $CATALINA_HOME/bin:$PATH  
RUN mkdir -p "$CATALINA_HOME"  
WORKDIR $CATALINA_HOME  
  
RUN apt-get update ; apt-get -y install curl ; apt-get clean  
  
# Get Tomcat  
# see https://www.apache.org/dist/tomcat/tomcat-8/KEYS  
RUN gpg --keyserver pool.sks-keyservers.net --recv-keys \  
05AB33110949707C93A279E3D3EFE6B686867BA6 \  
07E48665A34DCAFAE522E5E6266191C37C037D42 \  
47309207D818FFD8DCD3F83F1931D684307A10A5 \  
541FBE7D8F78B25E055DDEE13C370389288584E7 \  
61B832AC2F1C5A90F0F9B00A1C506407564C17A3 \  
79F7026C690BAA50B92CD8B66A3AD3F4F22C4FED \  
80FF76D88A969FE46108558A80B953A041E49465 \  
8B39757B1D8A994DF2433ED58B3A601F08C975E5 \  
A27677289986DB50844682F8ACB77FC2E86E29AC \  
A9C5DF4D22E99998D9875A5110C01C5A2F6059E7 \  
B3F49CD3B9BD2996DA90F817ED3873F5D3262722 \  
DCFD35E0BF8CA7344752DE8B6FB21E8933C60243 \  
F3A04C595DB5B6A5F1ECA43E3B7BBB100D811BBE \  
F7DA48BB64BCB84ECBA7EE6935CD23C10D498E23  
  
ENV TOMCAT_MAJOR 6  
ENV TOMCAT_VERSION 6.0.44  
ENV TOMCAT_TGZ_URL
https://www.apache.org/dist/tomcat/tomcat-$TOMCAT_MAJOR/v$TOMCAT_VERSION/bin/apache-
tomcat-$TOMCAT_VERSION.tar.gz  
  
RUN set -x \  
&& curl -fSL "$TOMCAT_TGZ_URL" -o tomcat.tar.gz \  
&& curl -fSL "$TOMCAT_TGZ_URL.asc" -o tomcat.tar.gz.asc \  
&& gpg --verify tomcat.tar.gz.asc \  
&& tar -xvf tomcat.tar.gz --strip-components=1 \  
&& rm bin/*.bat \  
&& rm tomcat.tar.gz*  
  
# Populate $CMS_HOME  
RUN mkdir /cms.home  
RUN rm -rf /usr/local/tomcat/webapps/*  
  
# Get the jdbc driver  
ENV JDBC_VERSION 9.4-1203.jdbc4  
RUN curl https://jdbc.postgresql.org/download/postgresql-$JDBC_VERSION.jar -o
$CATALINA_HOME/lib/postgresql-$JDBC_VERSION.jar  
  
COPY context.xml $CATALINA_HOME/conf/context.xml  
COPY server.xml $CATALINA_HOME/conf/server.xml  
  
COPY launcher.sh /launcher.sh  
RUN chmod +x /launcher.sh  
  
EXPOSE 8080 8009  
CMD ["/launcher.sh"]

