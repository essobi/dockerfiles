FROM hermsi/alpine-glibc  
  
LABEL maintainer "https://github.com/hermsi1337"  
  
ENV TS_USER=teamspeak \  
TS_HOME=/teamspeak  
  
# Get some stuff in order to work properly  
RUN set -x \  
&& apk update \  
&& apk --no-cache add ca-certificates wget openssl bash \  
&& update-ca-certificates \  
&& apk --no-cache --virtual .build-dependencies add w3m bzip2  
  
RUN addgroup -S \  
-g 503 \  
$TS_USER \  
&& adduser -S \  
-u 503 \  
-G $TS_USER \  
-D \  
$TS_USER  
  
WORKDIR ${TS_HOME}  
  
# Get teamspeak package  
RUN TS_SERVER_VER="$(w3m -dump https://www.teamspeak.com/downloads | grep -m 1
'Server 64-bit ' | awk '{print $NF}')" \  
&& wget
http://dl.4players.de/ts/releases/${TS_SERVER_VER}/teamspeak3-server_linux_amd64-${TS_SERVER_VER}.tar.bz2
-O /tmp/teamspeak.tar.bz2 \  
&& tar jxf /tmp/teamspeak.tar.bz2 -C /tmp \  
&& mv /tmp/teamspeak3-server_*/* ${TS_HOME}  
  
# Clean up  
RUN set -x \  
&& rm /tmp/teamspeak.tar.bz2 \  
&& apk del .build-dependencies \  
&& rm -rf /tmp/*  
  
RUN cp "$(pwd)/redist/libmariadb.so.2" $(pwd)  
  
ADD entrypoint.sh ${TS_HOME}/entrypoint.sh  
  
RUN chown -R ${TS_USER}:${TS_USER} ${TS_HOME} && chmod +x entrypoint.sh  
  
USER ${TS_USER}  
  
EXPOSE 9987/udp  
EXPOSE 10011  
EXPOSE 30033  
ENTRYPOINT ["./entrypoint.sh"]  

