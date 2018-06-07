FROM frolvlad/alpine-glibc:alpine-3.5_glibc-2.24  
# Add "app" user  
RUN mkdir -p /tmp/empty \  
&& addgroup -g 9999 app \  
&& adduser -G app -u 9999 -D app \  
&& rmdir /tmp/empty  
  
# Prepare data volume  
RUN mkdir -p /data && chown app:app /data  
WORKDIR /data  
  
ARG TS3SERVER_VERSION="3.0.13.8"  
ARG
TS3SERVER_URL="http://teamspeak.gameserver.gamed.de/ts3/releases/${TS3SERVER_VERSION}/teamspeak3-server_linux_amd64-${TS3SERVER_VERSION}.tar.bz2"  
#ARG
TS3SERVER_URL="http://dl.4players.de/ts/releases/${TS3SERVER_VERSION}/teamspeak3-server_linux_amd64-${TS3SERVER_VERSION}.tar.bz2"  
ARG
TS3SERVER_SHA384="e064dea24c1d5d4a5b9ce51c40ca977ddb5018c82cedf1508b41810d535693979555d5ec38027c30de818f5219c42bdc"  
ARG TS3SERVER_TAR_ARGS="-j"  
ARG TS3SERVER_INSTALL_DIR="/opt/ts3server"  
# Set up server  
ADD ${TS3SERVER_URL} "/ts3server.tar.bz2"  
RUN \  
apk --no-cache add \  
bash \  
tzdata \  
&& apk --no-cache add --virtual .build-deps \  
coreutils \  
tar \  
bzip2 \  
gzip \  
xz \  
\  
&& TS3SERVER_ACTUAL_SHA384="$(sha384sum /ts3server.tar.bz2 | awk '{print
$1}')" \  
&& if [ "${TS3SERVER_ACTUAL_SHA384}" != "${TS3SERVER_SHA384}" ]; then \  
echo "Invalid checksum: ${TS3SERVER_ACTUAL_SHA384} != ${TS3SERVER_SHA384}"
>&2; \  
exit 1; \  
fi \  
\  
&& mkdir -vp "${TS3SERVER_INSTALL_DIR}" \  
&& tar -v -C "${TS3SERVER_INSTALL_DIR}" -xf /ts3server.tar.bz2 --strip 1 \  
${TS3SERVER_TAR_ARGS} teamspeak3-server_linux_amd64/ \  
&& mv -v "${TS3SERVER_INSTALL_DIR}"/redist/libmariadb*.so*
"${TS3SERVER_INSTALL_DIR}" \  
&& rm -vfr \  
/ts3server.tar.bz2 \  
"${TS3SERVER_INSTALL_DIR}"/*.sh \  
"${TS3SERVER_INSTALL_DIR}"/CHANGELOG \  
"${TS3SERVER_INSTALL_DIR}"/doc \  
"${TS3SERVER_INSTALL_DIR}"/redist \  
"${TS3SERVER_INSTALL_DIR}"/serverquerydocs \  
"${TS3SERVER_INSTALL_DIR}"/tsdns \  
&& chown -v root:root -R "${TS3SERVER_INSTALL_DIR}" \  
&& chmod -v g-w,o-w -R "${TS3SERVER_INSTALL_DIR}" \  
\  
&& ln -vs ${TS3SERVER_INSTALL_DIR}/ts3server /usr/local/bin/ts3server \  
\  
&& apk --no-cache del .build-deps \  
&& rm -vfr \  
/tmp/* \  
/var/tmp/* \  
/var/lib/apt/lists/*  
  
# Healthcheck  
COPY healthcheck.sh /usr/local/bin/ts3server-healthcheck  
RUN \  
chmod +x /usr/local/bin/ts3server-healthcheck \  
&& sed -i 's,\r,,g' /usr/local/bin/ts3server-healthcheck  
HEALTHCHECK \--interval=30s --timeout=3s \  
CMD ts3server-healthcheck  
  
# Prepare runtime  
ENV LD_LIBRARY_PATH ${TS3SERVER_INSTALL_DIR}  
USER app  
# Can't use $TS3SERVER_INSTALL_DIR here because ENTRYPOINT does not accept
variables  
ENTRYPOINT [ "ts3server", "dbsqlpath=/opt/ts3server/sql/",
"query_ip_whitelist=/data/query_ip_whitelist.txt",
"query_ip_blacklist=/data/query_ip_blacklist.txt", "createinifile=1" ]  
  
EXPOSE 9987/udp 10011 30033 41144  

