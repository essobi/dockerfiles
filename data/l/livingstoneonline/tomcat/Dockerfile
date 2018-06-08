FROM livingstoneonline/oracle-jdk  
MAINTAINER Nigel Banks <nigel.g.banks@gmail.com>  
  
LABEL "License"="GPLv1" \  
"Version"="0.0.1"  
  
EXPOSE 8080  
ENV CATALINA_HOME=/opt/tomcat \  
FEDORA_HOME=/opt/fedora \  
SOLR_HOME=/opt/solr \  
DJATOKA_HOME=/opt/adore-djatoka \  
KAKADU_HOME=/opt/adore-djatoka/bin/Linux-x86-64 \  
PATH=/opt/tomcat/bin:$PATH \  
CATALINA_OPTS="-server -XX:+CMSClassUnloadingEnabled -Djava.awt.headless=true
-Djava.security.egd=file:/dev/urandom -Dkakadu.home=/opt/adore-
djatoka/bin/Linux-x86-64 -DLD_LIBRARY_PATH=/opt/adore-djatoka/lib/Linux-x86-64
-Djava.library.path=/opt/adore-djatoka/lib/Linux-x86-64"  
# Add Tomcat user.  
RUN mkdir -p ${CATALINA_HOME} && \  
addgroup tomcat && \  
adduser --system --disabled-password --no-create-home --ingroup tomcat --shell
/sbin/nologin --home ${CATALINA_HOME} tomcat  
  
WORKDIR ${CATALINA_HOME}  
  
# see https://www.apache.org/dist/tomcat/tomcat-$TOMCAT_MAJOR/KEYS  
RUN for key in \  
05AB33110949707C93A279E3D3EFE6B686867BA6 \  
07E48665A34DCAFAE522E5E6266191C37C037D42 \  
47309207D818FFD8DCD3F83F1931D684307A10A5 \  
541FBE7D8F78B25E055DDEE13C370389288584E7 \  
61B832AC2F1C5A90F0F9B00A1C506407564C17A3 \  
713DA88BE50911535FE716F5208B0AB1D63011C7 \  
79F7026C690BAA50B92CD8B66A3AD3F4F22C4FED \  
9BA44C2621385CB966EBA586F72C284D731FABEE \  
A27677289986DB50844682F8ACB77FC2E86E29AC \  
A9C5DF4D22E99998D9875A5110C01C5A2F6059E7 \  
DCFD35E0BF8CA7344752DE8B6FB21E8933C60243 \  
F3A04C595DB5B6A5F1ECA43E3B7BBB100D811BBE \  
F7DA48BB64BCB84ECBA7EE6935CD23C10D498E23 \  
; do \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key"; \  
done  
  
ARG TOMCAT_VERSION=7.0.82  
RUN curl -fSL
"https://www.apache.org/dyn/closer.cgi?action=download&filename=tomcat/tomcat-${TOMCAT_VERSION%%.*}/v${TOMCAT_VERSION}/bin/apache-
tomcat-${TOMCAT_VERSION}.tar.gz" -o tomcat.tar.gz && \  
curl -fSL
"https://www.apache.org/dist/tomcat/tomcat-${TOMCAT_VERSION%%.*}/v${TOMCAT_VERSION}/bin/apache-
tomcat-${TOMCAT_VERSION}.tar.gz.asc" -o tomcat.tar.gz.asc && \  
gpg --batch --verify tomcat.tar.gz.asc tomcat.tar.gz && \  
tar -xvf tomcat.tar.gz --strip-components=1 && \  
rm -fr tomcat.tar.gz* bin/*.bat webapps/docs webapps/examples  
  
# Cron is required to cleanup old files periodically.  
# MySQL is a dependancies requried to setup Fedora.  
RUN apt-install cron mysql-client && \  
cleanup  
  
# All wars and dependancies are installed by this copy.  
COPY rootfs /  
  
RUN chown -R tomcat:tomcat ${CATALINA_HOME} ${FEDORA_HOME} ${SOLR_HOME}
${DJATOKA_HOME}  

