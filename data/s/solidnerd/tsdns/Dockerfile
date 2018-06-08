FROM solidnerd/alpine-glibc:2.23-r3  
  
MAINTAINER Niclas Mietz <github@mietz.io>  
  
ENV TS_VERSION=3.0.13.6 \  
TS_FILENAME=teamspeak3-server_linux_amd64 \  
TSDNS_USER=tsdns \  
TSDNS_HOME=/tsdns \  
TSDNS_UID=1000 \  
TSDNS_GID=1000  
RUN addgroup -S $TSDNS_USER -g ${TSDNS_GID} \  
&& adduser -S \  
-g $TSDNS_USER \  
-h $TSDNS_HOME \  
-u ${TSDNS_UID} \  
$TSDNS_USER  
  
RUN apk add --no-cache wget mysql-client bzip2 \  
&& wget
"http://dl.4players.de/ts/releases/${TS_VERSION}/${TS_FILENAME}-${TS_VERSION}.tar.bz2"
-O ${TS_FILENAME}-${TS_VERSION}.tar.bz2 \  
&& tar -xjf "${TS_FILENAME}-${TS_VERSION}.tar.bz2" \  
&& rm ${TS_FILENAME}-${TS_VERSION}.tar.bz2 \  
&& mkdir -p ${TSDNS_HOME} \  
&& mv ${TS_FILENAME}/tsdns/* ${TSDNS_HOME} \  
&& rm -r ${TS_FILENAME}  
  
USER ${TSDNS_USER}  
  
WORKDIR ${TSDNS_HOME}  
  
ENTRYPOINT ["./tsdnsserver"]  
  
EXPOSE 41144/tcp  

