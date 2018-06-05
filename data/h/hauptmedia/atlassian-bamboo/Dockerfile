FROM debian:stretch  
MAINTAINER Julian Haupt <julian.haupt@hauptmedia.de>  
  
ENV BAMBOO_VERSION 6.4.0  
ENV MYSQL_CONNECTOR_J_VERSION 5.1.45  
ENV BAMBOO_USER bamboo  
ENV BAMBOO_HOME /var/atlassian/application-data/bamboo  
ENV BAMBOO_INSTALL_DIR /opt/atlassian/bamboo  
  
ENV SENCHA_CMD_VERSION 6.2.0  
ENV SENCHA_CMD_FILENAME SenchaCmd-${SENCHA_CMD_VERSION}-linux-amd64  
ENV SENCHA_CMD_DOWNLOAD_URL
http://cdn.sencha.com/cmd/${SENCHA_CMD_VERSION}/no-
jre/${SENCHA_CMD_FILENAME}.sh.zip  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# install needed debian packages & clean up  
RUN apt-get update && \  
apt-get install -y --no-install-recommends \  
gnupg libio-socket-ssl-perl sendemail libcrypt-ssleay-perl curl wget tar
xmlstarlet ca-certificates \  
git openssh-client libapparmor1 libsqlite3-0 libsqlite3-0 rsync ruby build-
essential \  
apt-transport-https lsb-release unzip dirmngr libfreetype6 libfontconfig1
libltdl7 maven wget && \  
wget -O /etc/apt/trusted.gpg.d/php.gpg https://packages.sury.org/php/apt.gpg
&& \  
echo "deb https://packages.sury.org/php/ $(lsb_release -sc) main" | tee
/etc/apt/sources.list.d/php.list && \  
apt-get update && \  
apt-get install -y --force-yes php7.2-cli php7.2-mysqlnd php7.2-curl php7.2-gd
php7.2-sqlite php7.2-xml php7.2-dom php7.2-bcmath php7.2-fpm php7.2-gmp
php7.2-mbstring php-pear && \  
apt-get clean autoclean && \  
apt-get autoremove --yes && \  
rm -rf /var/lib/{apt,dpkg,cache,log}/  
  
RUN echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" |
tee /etc/apt/sources.list.d/webupd8team-java.list && \  
echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" |
tee -a /etc/apt/sources.list.d/webupd8team-java.list && \  
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys EEA14886 && \  
apt-get update && \  
echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-set-
selections && \  
echo debconf shared/accepted-oracle-license-v1-1 seen true | debconf-set-
selections && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y --force-yes oracle-
java8-installer oracle-java8-set-default && \  
rm -rf /var/cache/oracle-jdk8-installer && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
  
# Adding letsencrypt-ca to truststore  
RUN export KEYSTORE=$JAVA_HOME/jre/lib/security/cacerts && \  
wget -P /tmp/ https://letsencrypt.org/certs/letsencryptauthorityx1.der && \  
wget -P /tmp/ https://letsencrypt.org/certs/letsencryptauthorityx2.der && \  
wget -P /tmp/ https://letsencrypt.org/certs/lets-encrypt-x1-cross-signed.der
&& \  
wget -P /tmp/ https://letsencrypt.org/certs/lets-encrypt-x2-cross-signed.der
&& \  
wget -P /tmp/ https://letsencrypt.org/certs/lets-encrypt-x3-cross-signed.der
&& \  
wget -P /tmp/ https://letsencrypt.org/certs/lets-encrypt-x4-cross-signed.der
&& \  
keytool -trustcacerts -keystore $KEYSTORE -storepass changeit -noprompt
-importcert -alias isrgrootx1 -file /tmp/letsencryptauthorityx1.der && \  
keytool -trustcacerts -keystore $KEYSTORE -storepass changeit -noprompt
-importcert -alias isrgrootx2 -file /tmp/letsencryptauthorityx2.der && \  
keytool -trustcacerts -keystore $KEYSTORE -storepass changeit -noprompt
-importcert -alias letsencryptauthorityx1 -file /tmp/lets-encrypt-x1-cross-
signed.der && \  
keytool -trustcacerts -keystore $KEYSTORE -storepass changeit -noprompt
-importcert -alias letsencryptauthorityx2 -file /tmp/lets-encrypt-x2-cross-
signed.der && \  
keytool -trustcacerts -keystore $KEYSTORE -storepass changeit -noprompt
-importcert -alias letsencryptauthorityx3 -file /tmp/lets-encrypt-x3-cross-
signed.der && \  
keytool -trustcacerts -keystore $KEYSTORE -storepass changeit -noprompt
-importcert -alias letsencryptauthorityx4 -file /tmp/lets-encrypt-x4-cross-
signed.der  
  
# add docker-entrypoint.sh script  
# install mono  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys
3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF && \  
echo "deb http://download.mono-project.com/repo/debian stretch main"
>/etc/apt/sources.list.d/mono-official.list && \  
apt-get update && \  
apt-get install -y mono-devel nuget  
  
# add nodejs upstream repo  
RUN (curl -sL https://deb.nodesource.com/setup_8.x | bash -) && \  
apt-get update && \  
apt-get install -y --no-install-recommends nodejs && \  
ln -s /usr/bin/nodejs /usr/local/bin/node && \  
apt-get clean autoclean && \  
apt-get autoremove --yes && \  
rm -rf /var/lib/{apt,dpkg,cache,log}/  
  
RUN npm install -g yarn grunt grunt-cli apidoc && \  
rm -rf /tmp/*  
  
# create bamboo user  
RUN mkdir -p ${BAMBOO_HOME} && \  
useradd --home ${BAMBOO_HOME} --shell /bin/bash --comment "Bamboo User"
${BAMBOO_USER} && \  
chown -R ${BAMBOO_USER} ${BAMBOO_HOME} /opt  
  
# run the following commands with this user and group  
USER ${BAMBOO_USER}  
  
# integrate SenchaCmd (do this after we changed the user)  
RUN curl -L --silent -o /tmp/${SENCHA_CMD_FILENAME}.sh.zip
${SENCHA_CMD_DOWNLOAD_URL} && \  
unzip /tmp/${SENCHA_CMD_FILENAME}.sh.zip -d /tmp && \  
rm /tmp/${SENCHA_CMD_FILENAME}.sh.zip && \  
chmod +x /tmp/SenchaCmd-* && \  
$(find /tmp -name "SenchaCmd-*" -print -quit) -dir /opt/SenchaCmd -q && \  
rm -rf /tmp/*  
  
# download and extract bamboo & configure git  
RUN mkdir -p ${BAMBOO_INSTALL_DIR} && \  
curl -L --silent
http://www.atlassian.com/software/bamboo/downloads/binary/atlassian-
bamboo-${BAMBOO_VERSION}.tar.gz | tar -xz --strip=1 -C ${BAMBOO_INSTALL_DIR}
&& \  
echo -e "\nbamboo.home=$BAMBOO_HOME" >> "${BAMBOO_INSTALL_DIR}/atlassian-
bamboo/WEB-INF/classes/bamboo-init.properties" && \  
git config --global http.sslVerify false  
  
# integrate mysql connector j library  
RUN curl -L --silent http://dev.mysql.com/get/Downloads/Connector-J/mysql-
connector-java-${MYSQL_CONNECTOR_J_VERSION}.tar.gz | tar -xz --strip=1 -C /tmp
&& \  
cp /tmp/mysql-connector-java-${MYSQL_CONNECTOR_J_VERSION}-bin.jar
${BAMBOO_INSTALL_DIR}/lib && \  
rm -rf /tmp/*  
  
COPY docker-entrypoint.sh ${BAMBOO_INSTALL_DIR}/bin/  
  
# HTTP Port  
EXPOSE 8085  
# Remote Agent port  
EXPOSE 54663  
WORKDIR ${BAMBOO_INSTALL_DIR}  
  
# run the entrypoint as root  
USER root:root  
  
ENTRYPOINT ["bin/docker-entrypoint.sh"]  
CMD ["bin/start-bamboo.sh", "-fg"]  

