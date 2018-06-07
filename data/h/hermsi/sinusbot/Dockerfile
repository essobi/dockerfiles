FROM debian:stable-slim  
  
LABEL maintainer "https://github.com/hermsi1337"  
  
ENV SINUSBOT_DIR="/ts3soundboard" \  
SINUSBOT_USER="sinusbot" \  
SINUSBOT_GROUP="sinusbot" \  
SINUSBOT_DOWNLOAD="https://www.sinusbot.com/dl/sinusbot-beta.tar.bz2" \  
TEAMSPEAK_DOWNLOAD="http://dl.4players.de/ts/releases" \  
TEAMSPEAK_CLIENT="TeamSpeak3-Client-linux_amd64" \  
TEAMSPEAK_VERSION="3.0.19.4" \  
YTDL_BIN="/usr/local/bin/youtube-dl"  
ENV SINUSBOT_DATA="${SINUSBOT_DIR}/data" \  
SINUSBOT_SCRIPTS="${SINUSBOT_DIR}/scripts" \  
TEAMSPEAK_CLIENT_DIR="${SINUSBOT_DIR}/${TEAMSPEAK_CLIENT}"  
RUN apt-get -q update && \  
apt-get -q -y --no-install-recommends install x11vnc xvfb libxcursor1 ca-
certificates bzip2 \  
libpulse0 libasound2 libglib2.0-0 libnss3 locales wget python less pulseaudio
&& \  
update-ca-certificates && \  
echo "LC_ALL=en_US.UTF-8" >> /etc/default/locale && \  
echo "LANG=en_US.UTF-8" >> /etc/default/locale && \  
locale-gen --purge en_US.UTF-8  
  
RUN groupadd -r \  
-g 1337 \  
"${SINUSBOT_GROUP}" && \  
useradd -r \  
-u 1337 \  
-g 1337 \  
-d "${SINUSBOT_DIR}" \  
"${SINUSBOT_USER}"  
  
WORKDIR "${SINUSBOT_DIR}"  
  
RUN wget -q "${SINUSBOT_DOWNLOAD}" -O "/tmp/sinusbot.tar.bz2" && \  
tar xjf "/tmp/sinusbot.tar.bz2" && \  
cp -r "${SINUSBOT_SCRIPTS}" "${SINUSBOT_SCRIPTS}.bak" && \  
cp "${SINUSBOT_DIR}/config.ini.dist" "${SINUSBOT_DIR}/config.ini" && \  
sed -i 's|^DataDir.*|DataDir = '"${SINUSBOT_DATA}"'|g'
"${SINUSBOT_DIR}/config.ini"  
  
RUN wget -q
"${TEAMSPEAK_DOWNLOAD}/${TEAMSPEAK_VERSION}/${TEAMSPEAK_CLIENT}-${TEAMSPEAK_VERSION}.run"
-O "/tmp/${TEAMSPEAK_CLIENT}.run" && \  
chmod 755 "/tmp/${TEAMSPEAK_CLIENT}.run" && \  
yes | "/tmp/${TEAMSPEAK_CLIENT}.run"  
  
RUN cp -f "${SINUSBOT_DIR}/plugin/libsoundbot_plugin.so"
"${TEAMSPEAK_CLIENT_DIR}/plugins/." && \  
sed -i "s|^TS3Path.*|TS3Path =
\"${TEAMSPEAK_CLIENT_DIR}/ts3client_linux_amd64\"|g"
"${SINUSBOT_DIR}/config.ini" && \  
wget -q "https://yt-dl.org/downloads/latest/youtube-dl" -O "${YTDL_BIN}" && \  
chmod 755 -f "${YTDL_BIN}" && \  
echo "YoutubeDLPath = \"${YTDL_BIN}\"" >> "${SINUSBOT_DIR}/config.ini"  
  
COPY "entrypoint.sh" "entrypoint.sh"  
  
RUN apt-get -q -y remove wget bzip2 && \  
apt-get -q -y autoremove && \  
apt-get -q -y autoclean && \  
apt-get -q -y purge && \  
apt-get -q -y clean all && \  
rm -rf "/tmp/*" "/var/lib/apt/lists/*" && \  
chown -R "${SINUSBOT_USER}":"${SINUSBOT_GROUP}" "${SINUSBOT_DIR}"
"${TEAMSPEAK_CLIENT_DIR}"  
  
VOLUME ["${SINUSBOT_DATA}", "${SINUSBOT_SCRIPTS}"]  
  
EXPOSE 8087  
ENTRYPOINT ["./entrypoint.sh"]  

