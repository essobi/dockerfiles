FROM centos:7  
# Installing openJDK  
RUN yum install -y java-1.7.0-openjdk wget mysql  
  
#Setting environment variables  
ENV CATALINA_HOME /usr/local/tomcat  
ENV PATH $CATALINA_HOME:$CATALINA_HOME/bin:$PATH  
  
#Setting WORKDIR  
RUN mkdir -p "$CATALINA_HOME"  
WORKDIR $CATALINA_HOME  
  
# see https://www.apache.org/dist/tomcat/tomcat-8/KEYS  
#RUN gpg --keyserver pool.sks-keyservers.net --recv-keys \  
# 05AB33110949707C93A279E3D3EFE6B686867BA6 \  
# 07E48665A34DCAFAE522E5E6266191C37C037D42 \  
# 47309207D818FFD8DCD3F83F1931D684307A10A5 \  
# 541FBE7D8F78B25E055DDEE13C370389288584E7 \  
# 61B832AC2F1C5A90F0F9B00A1C506407564C17A3 \  
# 713DA88BE50911535FE716F5208B0AB1D63011C7 \  
# 79F7026C690BAA50B92CD8B66A3AD3F4F22C4FED \  
# 9BA44C2621385CB966EBA586F72C284D731FABEE \  
# A27677289986DB50844682F8ACB77FC2E86E29AC \  
# A9C5DF4D22E99998D9875A5110C01C5A2F6059E7 \  
# DCFD35E0BF8CA7344752DE8B6FB21E8933C60243 \  
# F3A04C595DB5B6A5F1ECA43E3B7BBB100D811BBE \  
# F7DA48BB64BCB84ECBA7EE6935CD23C10D498E23  
  
ENV TOMCAT_MAJOR 7  
ENV TOMCAT_VERSION 7.0.67  
ENV TOMCAT_TGZ_URL
https://www.apache.org/dist/tomcat/tomcat-${TOMCAT_MAJOR}/v$TOMCAT_VERSION/bin/apache-
tomcat-$TOMCAT_VERSION.tar.gz  
  
RUN set -x \  
&& curl -fSL "$TOMCAT_TGZ_URL" -o tomcat.tar.gz \  
&& curl -fSL "$TOMCAT_TGZ_URL.asc" -o tomcat.tar.gz.asc \  
# && gpg --verify tomcat.tar.gz.asc \  
&& tar -xvf tomcat.tar.gz --strip-components=1 \  
&& rm bin/*.bat \  
&& rm tomcat.tar.gz* \  
&& rm -rf ./webapps/ROOT  
  
RUN wget -P ./lib http://central.maven.org/maven2/mysql/mysql-connector-
java/5.1.34/mysql-connector-java-5.1.34.jar && \  
wget -P ./lib http://central.maven.org/maven2/de/javakaffee/msm/memcached-
session-manager/1.8.3/memcached-session-manager-1.8.3.jar && \  
wget -P ./lib http://central.maven.org/maven2/de/javakaffee/msm/memcached-
session-manager-tc7/1.8.3/memcached-session-manager-tc7-1.8.3.jar && \  
wget -P ./lib
http://central.maven.org/maven2/net/spy/spymemcached/2.11.1/spymemcached-2.11.1.jar
&& \  
wget -P ./lib http://central.maven.org/maven2/org/apache/commons/commons-
lang3/3.3.1/commons-lang3-3.3.1.jar && \  
wget -P ./lib http://central.maven.org/maven2/commons-logging/commons-
logging/1.1.1/commons-logging-1.1.1.jar && \  
wget -P ./lib
http://java.net/projects/javamail/downloads/download/javax.mail.jar  
  
COPY ./conf/*.xml ./conf/  
COPY ./bin/setenv.sh ./bin/setenv.sh  
RUN chmod +x ./bin/setenv.sh  
  
COPY ./entrypoint.sh ./entrypoint.sh  
RUN chmod +x ./entrypoint.sh  
  
#Expose port 8080  
EXPOSE 8080  
CMD ["entrypoint.sh"]  

