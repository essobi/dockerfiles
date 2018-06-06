FROM ubuntu:16.04  
MAINTAINER "Rsrp Sinr" <rsrp.sinr@gmail.com>  
  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y \  
locales \  
&& rm -rf /var/lib/apt/lists/*  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
#---------------------------------------------  
# GuacamoleD  
#---------------------------------------------  
  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y \  
ca-certificates \  
wget \  
git \  
build-essential \  
curl \  
ldap-utils \  
libnss-ldap \  
libpam-ldap \  
expect \  
zip \  
inetutils-ping \  
openssh-server \  
&& rm -rf /var/lib/apt/lists/*  
#---------------------------------------------  
# Install Oracle JDK 1.8 (ver jdk1.8.0_111)  
#---------------------------------------------  
RUN mkdir -p /usr/java && \  
wget -qO -
https://www.dropbox.com/s/1eee6lcq87zub3b/jdk-8u111-linux-x64.tar.gz | tar xz
-C /usr/java && \  
ln -s /usr/java/jdk1.8.0_111 /usr/java/default  
ENV JAVA_HOME /usr/java/default  
ENV PATH $JAVA_HOME/bin:$PATH  
  
  
# Guacamole dependencies  
#---------------------------------------------  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y \  
libcairo2-dev libjpeg-turbo8-dev libpng12-dev libossp-uuid-dev libfreerdp-dev
libpango1.0-dev libssh2-1-dev libtelnet-dev \  
libvncserver-dev libpulse-dev libssl-dev libvorbis-dev libwebp-dev git build-
essential autoconf libtool tomcat8 \  
tomcat8-admin tomcat8-common tomcat8-docs tomcat8-user maven mysql-server
mysql-client mysql-common mysql-utilities libpulse-dev \  
libvorbis-dev freerdp ghostscript \  
&& rm -rf /var/lib/apt/lists/*  
# Guacamole server compile & install  
# ref: https://gist.github.com/cyrex562/6abbe01a82ddc654b0cff006dfa3d935  
#---------------------------------------------  
RUN git clone https://github.com/apache/incubator-guacamole-server.git
/opt/guacamole-server && \  
cd /opt/guacamole-server && \  
autoreconf -fi && \  
./configure \--with-init-dir=/etc/init.d && \  
make && \  
make install && \  
ldconfig  
  
RUN mkdir -p /etc/guacamole && \  
mkdir -p /etc/guacamole/lib && \  
mkdir -p /etc/guacamole/extensions  
  
# Guacamole client compile & install  
#---------------------------------------------  
RUN git clone https://github.com/apache/incubator-guacamole-client.git
/opt/guacamole-client && \  
cd /opt/guacamole-client && \  
mvn package && \  
cp ./guacamole/target/guacamole-*.war /var/lib/tomcat8/webapps/guacamole.war
&& \  
cp ./extensions/guacamole-auth-jdbc/modules/guacamole-auth-jdbc-
mysql/target/guacamole-auth-jdbc-mysql-*.jar /etc/guacamole/extensions/ && \  
cp ./extensions/guacamole-auth-ldap/target/guacamole-auth-ldap-*.jar
/etc/guacamole/extensions/  
  
RUN wget -qO /tmp/mysql-connector-java-5.1.40.tar.gz
https://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-
java-5.1.40.tar.gz && \  
cd /tmp && \  
tar xf mysql-conn* && \  
cp mysql-connector-java-5.1.40/mysql-connector-java-5.1.40-bin.jar
/etc/guacamole/lib/ && \  
ln -s /usr/local/lib/freerdp/* /usr/lib/x86_64-linux-gnu/freerdp/.  
  
RUN rm -rf /usr/share/tomcat8/.guacamole && \  
ln -s /etc/guacamole /usr/share/tomcat8/.guacamole  
  
# Set env vars  
#---------------------------------------------  
ENV GUACAMOLE_HOME "/etc/guacamole"  
# Perl  
#---------------------------------------------  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y \  
libxml2-dev \  
zlibc \  
zlib1g \  
zlib1g-dev &&\  
rm -rf /var/lib/apt/lists/* && \  
curl -L http://cpanmin.us | perl - App::cpanminus  
  
# Guacamole helper scripts  
#---------------------------------------------  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y \  
libdbd-mysql-perl \  
&& rm -rf /var/lib/apt/lists/*  
RUN cpanm JSON && \  
cpanm DBI  
ADD ensureLdapUsersInGuacaDb.pl /usr/bin/ensureLdapUsersInGuacaDb.pl  
RUN chmod a+x /usr/bin/ensureLdapUsersInGuacaDb.pl  
  
# xRdp & Mate  
#---------------------------------------------  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y \  
supervisor \  
xrdp \  
mate-core \  
mate-desktop-environment \  
mate-notification-daemon \  
mate-desktop-environment-extras \  
&& rm -rf /var/lib/apt/lists/*  
# Chrome browser  
#---------------------------------------------  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y \  
fonts-liberation \  
lsb-release \  
xdg-utils \  
&& rm -rf /var/lib/apt/lists/*  
RUN wget -qO /tmp/google-chrome-stable_current_amd64.deb
https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \  
dpkg -i /tmp/google-chrome-stable_current_amd64.deb && \  
rm -f /tmp/google-chrome-stable_current_amd64.deb  
  
ADD xrdp.ini /etc/xrdp/xrdp.ini  
  
# xRdp/Mate helper scripts  
#---------------------------------------------  
ADD ensureUserDirAndFiles.pl /usr/bin/ensureUserDirAndFiles.pl  
RUN chmod a+x /usr/bin/ensureUserDirAndFiles.pl  
  
# Kill Chrome helper script  
#---------------------------------------------  
ADD kill_chrome.pl /usr/bin/kill_chrome.pl  
ADD KillChrome.desktop /KillChrome.desktop  
RUN chmod +x /usr/bin/kill_chrome.pl && \  
chmod +x /KillChrome.desktop  
  
ENV GUACAMOLED_VERSION 0.3  
  
ADD entrypoint.sh /entrypoint.sh  
RUN chmod 700 /entrypoint.sh  
  
ADD app.sh /app.sh  
RUN chmod 700 /app.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  

