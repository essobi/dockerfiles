# ==================  
# Steam Dockerfile  
# PrivateHeberg©  
# ==================  
FROM ubuntu:xenial  
MAINTAINER PrivateHeberg (PHClement)  
  
ENV LANG="fr_FR.UTF-8" \  
LC_ALL="fr_FR.UTF-8 " \  
PORT=1023 \  
SINUS_USER="3000" \  
SINUS_GROUP="3000" \  
SINUS_DIR="/sinusbot" \  
YTDL_BIN="/usr/local/bin/youtube-dl" \  
YTDL_VERSION="latest" \  
TS3_VERSION="3.0.19.4" \  
TS3_DL_ADDRESS="http://teamspeak.gameserver.gamed.de/ts3/releases/" \  
SINUSBOT_DL_URL="https://cdn.privateheberg.com/SinusBot/sinus.tar.bz2"  
ENV SINUS_DATA="$SINUS_DIR/data" \  
SINUS_DATA_SCRIPTS="$SINUS_DIR/scripts" \  
TS3_DIR="$SINUS_DIR/TeamSpeak3-Client-linux_amd64"  
RUN groupadd -g "$SINUS_GROUP" sinusbot && \  
useradd -u "$SINUS_USER" -g "$SINUS_GROUP" -d "$SINUS_DIR" sinusbot && \  
apt-get -q update -y && \  
apt-get -q upgrade -y && \  
apt-get -q install -y libasound2 xcb xinit x11vnc xvfb libxcursor1 ca-
certificates bzip2 \  
libglib2.0-0 sqlite3 libnss3 locales wget sudo python less && \  
update-ca-certificates && \  
locale-gen --purge "$LANG" && \  
update-locale LANG="$LANG" && \  
echo "LC_ALL=en_US.UTF-8" >> /etc/default/locale && \  
echo "LANG=en_US.UTF-8" >> /etc/default/locale && \  
update-ca-certificates && \  
locale-gen --purge en_US.UTF-8 && \  
mkdir -p "$SINUS_DIR" && \  
wget -qO- "$SINUSBOT_DL_URL" | \  
tar -xjf- -C "$SINUS_DIR" && \  
sed -i 's|^DataDir.*|DataDir = '"$SINUS_DATA"'|g' "$SINUS_DIR/config.ini" && \  
mkdir -p "$TS3_DIR" && \  
cd "$SINUS_DIR" || exit 1 && \  
wget -q -O "TeamSpeak3-Client-linux_amd64-$TS3_VERSION.run" \  
"$TS3_DL_ADDRESS/$TS3_VERSION/TeamSpeak3-Client-linux_amd64-$TS3_VERSION.run"
&& \  
chmod 755 "TeamSpeak3-Client-linux_amd64-$TS3_VERSION.run" && \  
yes | "./TeamSpeak3-Client-linux_amd64-$TS3_VERSION.run" && \  
rm -f "TeamSpeak3-Client-linux_amd64-$TS3_VERSION.run" && \  
cp -f "$SINUS_DIR/plugin/libsoundbot_plugin.so" "$TS3_DIR/plugins/" && \  
sed -i "s|^TS3Path.*|TS3Path = \"$TS3_DIR/ts3client_linux_amd64\"|g"
"$SINUS_DIR/config.ini" && \  
sed -i "s|^ListenPort.*|ListenPort = "$PORT"|g" "$SINUS_DIR/config.ini" && \  
wget -q -O "$YTDL_BIN" "https://yt-dl.org/downloads/$YTDL_VERSION/youtube-dl"
&& \  
chmod 755 -f "$YTDL_BIN" && \  
echo "YoutubeDLPath = \"$YTDL_BIN\"" >> "$SINUS_DIR/config.ini" && \  
chown -fR sinusbot:sinusbot "$SINUS_DIR" && \  
apt-get -q clean all && \  
rm -rf /tmp/* /var/tmp/*  
  
COPY run.sh /run.sh  
RUN chmod 777 /run.sh  
  
VOLUME ["$SINUS_DATA", "$SINUS_DATA_SCRIPTS"]  
  
EXPOSE $PORT  
  
ENTRYPOINT ["/run.sh"]  

