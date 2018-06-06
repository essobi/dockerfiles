FROM islandora/claw-base  
MAINTAINER Nigel Banks <nigel.g.banks@gmail.com>  
  
LABEL "Description"="Islandora CLAW: Kitchen sink" \  
"License"="MIT" \  
"Version"="0.0.1"  
  
EXPOSE 80  
EXPOSE 8080  
EXPOSE 8181  
EXPOSE 3306  
ENV TERM=xterm  
  
#####################  
# Install Dockerize #  
#####################  
ARG DOCKERIZE_VERSION="0.2.0"  
RUN curl -L
https://github.com/jwilder/dockerize/releases/download/v${DOCKERIZE_VERSION}/dockerize-
linux-amd64-v${DOCKERIZE_VERSION}.tar.gz | \  
tar -xzf - -C /usr/local/bin  
  
##############################  
# Common Packages & devtools #  
##############################  
RUN apk-install git zsh vim bash the_silver_searcher && \  
cleanup  
  
##########  
# Apache #  
##########  
RUN apk-install apache2 apache2-utils apache2-proxy && \  
mkdir /run/apache2 && \  
chown -R apache:apache /var/www && \  
chmod 2775 /var/www/localhost && \  
cleanup  
  
###########  
# MariaDB #  
###########  
RUN apk-install mariadb mysql-client && \  
mkdir /run/mysqld && \  
chown mysql:mysql /run/mysqld && \  
cleanup  
  
#################  
# Java Open JDK #  
#################  
ENV JAVA_HOME=/usr/lib/jvm/default-jvm  
  
RUN apk-install openjdk8 && \  
cleanup  
  
#########  
# Maven #  
#########  
ARG MAVEN_VERSION="3.3.9"  
ENV M2_HOME=/opt/maven \  
PATH=${PATH}:/opt/maven/bin  
  
RUN curl -L
http://archive.apache.org/dist/maven/maven-${MAVEN_VERSION%%.*}/${MAVEN_VERSION}/binaries/apache-
maven-${MAVEN_VERSION}-bin.tar.gz | \  
tar -xzf - -C /opt && \  
mv /opt/apache-maven-${MAVEN_VERSION} ${M2_HOME}  
  
##########  
# Tomcat #  
##########  
ARG TOMCAT_VERSION="7.0.69"  
ENV CATALINA_HOME=/opt/tomcat \  
CATALINA_BASE=/opt/tomcat \  
CATALINA_OPTS="-server -XX:+CMSClassUnloadingEnabled -Djava.awt.headless=true
-Djava.security.egd=file:/dev/./urandom" \  
PATH=${PATH}:/opt/tomcat/bin  
  
RUN addgroup tomcat && \  
adduser -s /sbin/nologin -G tomcat -SDH -h ${CATALINA_HOME} tomcat  
  
RUN curl -L
http://archive.apache.org/dist/tomcat/tomcat-${TOMCAT_VERSION%%.*}/v${TOMCAT_VERSION}/bin/apache-
tomcat-${TOMCAT_VERSION}.tar.gz | \  
tar -xzf - -C /tmp && \  
mv /tmp/apache-tomcat-${TOMCAT_VERSION} ${CATALINA_HOME} && \  
rm -rf ${CATALINA_HOME}/webapps/docs && \  
rm -rf ${CATALINA_HOME}/webapps/examples && \  
cleanup  
  
##########  
# Fedora #  
##########  
ARG FEDORA_VERSION="4.4.0"  
ENV FEDORA_HOME="/mnt/fedora-data" \  
CATALINA_OPTS="${CATALINA_OPTS} -Dfcrepo.home=/mnt/fedora-data"  
RUN mkdir -p ${FEDORA_HOME} && \  
chown tomcat:tomcat ${FEDORA_HOME} && \  
curl -o ${CATALINA_BASE}/webapps/fcrepo.war \  
-L https://github.com/fcrepo4/fcrepo4/releases/download/fcrepo-${FEDORA_VERSION}/fcrepo-webapp-${FEDORA_VERSION}.war && \  
mkdir ${CATALINA_BASE}/webapps/fcrepo && \  
unzip -o ${CATALINA_BASE}/webapps/fcrepo.war -d
${CATALINA_HOME}/webapps/fcrepo && \  
rm -rf ${CATALINA_HOME}/webapps/*.war && \  
cleanup  
  
##############  
# Blazegraph #  
##############  
ARG BLAZEGRAPH_VERSION="1.5.1"  
ENV CATALINA_OPTS="${CATALINA_OPTS}
-Dcom.bigdata.rdf.sail.webapp.ConfigParams.propertyFile=${CATALINA_BASE}/webapps/bigdata/WEB-
INF/RWStore.properties"  
RUN curl -o ${CATALINA_BASE}/webapps/bigdata.war \  
-L http://sourceforge.net/projects/bigdata/files/bigdata/${BLAZEGRAPH_VERSION}/bigdata.war/download && \  
mkdir ${CATALINA_BASE}/webapps/bigdata && \  
unzip -o ${CATALINA_BASE}/webapps/bigdata.war -d
${CATALINA_HOME}/webapps/bigdata && \  
rm -rf ${CATALINA_HOME}/webapps/*.war && \  
mkdir /opt/blazegraph && \  
chown tomcat:tomcat /opt/blazegraph && \  
cleanup  
  
########  
# Solr #  
########  
ARG SOLR_VERSION="4.10.4"  
ARG SOLR_DEPENDENCIES="log4j-1.2.17.jar slf4j-api-1.7.6.jar
slf4j-log4j12-1.7.6.jar"  
ENV SOLR_HOME=/opt/solr  
  
RUN curl -L
http://archive.apache.org/dist/lucene/solr/${SOLR_VERSION}/solr-${SOLR_VERSION}.tgz
| \  
tar -xzf - -C /tmp && \  
mkdir ${CATALINA_BASE}/webapps/solr && \  
cp /tmp/solr-${SOLR_VERSION}/dist/solr-${SOLR_VERSION}.war
${CATALINA_BASE}/webapps/solr.war && \  
unzip -o ${CATALINA_BASE}/webapps/solr.war -d ${CATALINA_BASE}/webapps/solr &&
\  
for dep in $SOLR_DEPENDENCIES; do \  
cp /tmp/solr-${SOLR_VERSION}/example/lib/ext/$dep ${CATALINA_BASE}/lib; \  
done && \  
curl -o ${CATALINA_BASE}/lib/commons-logging-1.1.2.jar \  
-L http://repo1.maven.org/maven2/commons-logging/commons-logging/1.1.2/commons-logging-1.1.2.jar && \  
mkdir ${SOLR_HOME} && \  
cp -a /tmp/solr-${SOLR_VERSION}/example/solr/* ${SOLR_HOME}/ && \  
curl -L https://ftp.drupal.org/files/projects/apachesolr-7.x-1.8.tar.gz | \  
tar -xzf - -C /tmp && \  
cp -r /tmp/apachesolr/solr-conf/solr-4.x/* ${SOLR_HOME}/collection1/conf && \  
chown -R tomcat:tomcat ${SOLR_HOME} && \  
rm -rf ${CATALINA_HOME}/webapps/*.war && \  
cleanup  
  
#########  
# Karaf #  
#########  
ARG KARAF_VERSION="4.0.4"  
ENV KARAF_HOME="/opt/karaf" \  
KARAF_OPTS="-Xms128M -Xmx512M -XX:+UnlockDiagnosticVMOptions
-XX:+UnsyncloadClass" \  
PATH=${PATH}:/opt/karaf/bin  
  
RUN addgroup karaf && \  
adduser -s /sbin/nologin -G karaf -DH -h ${KARAF_HOME} karaf  
  
RUN apk-install openssh && \  
curl -L http://archive.apache.org/dist/karaf/${KARAF_VERSION}/apache-
karaf-${KARAF_VERSION}.tar.gz | \  
tar -xzf - -C /tmp && \  
mv /tmp/apache-karaf-${KARAF_VERSION} /opt/karaf && \  
cleanup  
  
#######  
# PHP #  
#######  
RUN apk-install \  
php-apache2 \  
php-ctype \  
php-curl \  
php-gd \  
php-json \  
php-mysql \  
php-openssl \  
php-pdo \  
php-pdo_mysql \  
php-pear \  
php-phar \  
php-posix \  
php-soap \  
php-xml \  
php-xmlreader \  
php-xsl && \  
cleanup  
  
# This is a temporary measure until we create our own APK package for
php5-stomp  
RUN apk-install make autoconf gcc openssl-dev php-dev libc-dev && \  
touch /etc/php/conf.d/stomp.ini && \  
pear config-set php_ini /etc/php/conf.d/stomp.ini && \  
pear install pecl/stomp && \  
pear config-set php_ini /etc/php/php.ini && \  
apk-uninstall make autoconf gcc openssl-dev php-dev libc-dev && \  
cleanup  
  
############  
# Composer #  
############  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin && \  
mv /usr/local/bin/composer.phar /usr/local/bin/composer && \  
chmod a+x /usr/local/bin/composer  
  
#########  
# Drush #  
#########  
ARG DRUSH_VERSION="8.0.2"  
RUN curl -L -o /usr/local/bin/drush https://github.com/drush-
ops/drush/releases/download/${DRUSH_VERSION}/drush.phar && \  
chmod a+x /usr/local/bin/drush  
  
##########  
# Drupal #  
##########  
ARG DRUPAL_VERSION="7.43"  
ENV DRUPAL_ROOT=/var/www/localhost/htdocs  
  
RUN drush dl -y --destination=/var/www/localhost --drupal-project-
rename=htdocs drupal-${DRUPAL_VERSION} && \  
mkdir ${DRUPAL_ROOT}/sites/all/modules/contrib && \  
mkdir ${DRUPAL_ROOT}/sites/all/modules/custom && \  
mkdir ${DRUPAL_ROOT}/sites/all/modules/features && \  
chown apache:apache ${DRUPAL_ROOT} && \  
cleanup  
  
RUN curl -L https://github.com/Islandora-
CLAW/claw_install_profile/archive/master.tar.gz | \  
tar -xzf - -C ${DRUPAL_ROOT}/profiles && \  
mv ${DRUPAL_ROOT}/profiles/claw_install_profile-master
${DRUPAL_ROOT}/profiles/claw_install_profile && \  
mkdir ${DRUPAL_ROOT}/sites/all/libraries/ARC2 && \  
cd ${DRUPAL_ROOT} && drush make -y --concurrency=4 --no-cache \  
${DRUPAL_ROOT}/profiles/claw_install_profile/claw_install_profile.make && \  
mv ${DRUPAL_ROOT}/sites/all/libraries/ARC2/arc2
${DRUPAL_ROOT}/sites/all/libraries/ARC2/arc && \  
cleanup  
  
####################  
# CLAW Github Repo #  
####################  
ENV CLAW_HOME=/opt/claw  
  
# Git sub-module's require Perl.  
RUN apk-install perl  
  
RUN git clone https://github.com/Islandora-CLAW/CLAW.git ${CLAW_HOME} && \  
cd ${CLAW_HOME} && git submodule update --init --recursive && \  
chmod -R a+rx ${CLAW_HOME}  
  
###############################  
# Download Maven Dependencies #  
###############################  
RUN cd ${CLAW_HOME}/Alpaca/commands && composer install && \  
cd ${CLAW_HOME}/Alpaca && mvn clean install
-Dmaven.repo.local=${M2_HOME}/repository  
  
#####################  
# Islandora Modules #  
#####################  
# This is a temporary measure until we split up the repo into submodules.  
# We will eventually make it part of the drush make file like everything else.  
RUN ln -s ${CLAW_HOME}/islandora ${DRUPAL_ROOT}/sites/all/modules/islandora &&
\  
chown -R apache:apache ${CLAW_HOME}/islandora && \  
chmod -R g+rw ${CLAW_HOME}  
  
#############  
# Oh My ZSH #  
#############  
RUN git clone https://github.com/robbyrussell/oh-my-zsh.git /root/.oh-my-zsh
&& \  
rm -fr /root/.oh-my-zsh/.git && \  
cp /root/.oh-my-zsh/templates/zshrc.zsh-template ~/.zshrc  
  
##############  
# Filesystem #  
##############  
COPY rootfs /  

