FROM java:8-jre  
  
LABEL maintainer="Alexander Trost <galexrt@googlemail.com>"  
  
ENV JTS3_USER="3000" \  
JTS3_GROUP="3000" \  
JTS3_DIR="/jts3servermod" \  
JTS3_JAVA_ARGS="-Xmx256M" \  
GOSU_VERSION="1.10" \  
ARCH=""  
RUN [ ! -z "$ARCH" ] || ARCH="$(dpkg --print-architecture)" && \  
groupadd -g "$JTS3_GROUP" -r jts3servermod && \  
useradd -u "$JTS3_USER" -r -g "$JTS3_GROUP" -d "$JTS3_DIR" jts3servermod && \  
apt-get -q update && \  
apt-get -q upgrade -y && \  
apt-get -q install unzip -y && \  
wget -q -O "/tmp/jts3servermod.zip"
"http://www.stefan1200.de/dlrequest.php?file=jts3servermod&type=.zip" && \  
cd /tmp && \  
unzip "/tmp/jts3servermod.zip" && \  
mv "/tmp/JTS3ServerMod" "$JTS3_DIR" && \  
chown -R jts3servermod:jts3servermod "$JTS3_DIR" && \  
rm -rf "$JTS3_DIR/jts3servermod.zip" "$JTS3_DIR/tools" "$JTS3_DIR/readme*"
"$JTS3_DIR/documents" "$JTS3_DIR/changelog.txt" && \  
cp -rf "$JTS3_DIR/config" "$JTS3_DIR/default_config" && \  
wget -O /usr/local/bin/gosu
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$ARCH" &&
\  
wget -O /usr/local/bin/gosu.asc
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$ARCH.asc"
&& \  
export GNUPGHOME="$(mktemp -d)" && \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 && \  
gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu && \  
rm -r "$GNUPGHOME" /usr/local/bin/gosu.asc && \  
chmod +x /usr/local/bin/gosu && \  
gosu nobody true && \  
apt-get -qq clean && \  
apt-get -qq autoremove --purge -y && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
VOLUME ["$JTS3_DIR/config"]  
  
COPY entrypoint.sh /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  

