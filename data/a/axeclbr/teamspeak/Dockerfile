FROM orimani/alpine-glibc  
  
MAINTAINER axeclbr <axeclbr@posteo.de>  
  
RUN export \  
TS_CHECKSUM="51eff1023549140fec592cb140edb0670c11cbf9" \  
TS_URL="http://dl.4players.de/ts/releases/3.0.12.2/teamspeak3-server_linux_amd64-3.0.12.2.tar.bz2"
\  
&& apk --update add curl \  
&& curl -L $TS_URL -o /tmp/teamspeak.tar.bz2 \  
&& if [ $(sha1sum /tmp/teamspeak.tar.bz2 | awk {'print $1'}) != $TS_CHECKSUM
]; then echo "CHECKSUM CHECK FAILED: teamspeak"; exit 1; fi \  
&& mkdir /opt \  
&& tar xjf /tmp/teamspeak.tar.bz2 -C /opt \  
&& mv /opt/teamspeak3-server_* /opt/teamspeak \  
&& addgroup -g 503 teamspeak \  
&& adduser -u 503 -G teamspeak -h /opt/teamspeak -S -D teamspeak \  
&& ln -s /data/ts3server.sqlitedb /opt/teamspeak/ts3server.sqlitedb \  
&& chown -R teamspeak:teamspeak /opt/teamspeak \  
&& apk del curl \  
&& rm -rf \  
/tmp/teamspeak.tar.bz2 \  
/var/cache/apk*  
  
EXPOSE 9987/udp 10011 30033  
  
USER teamspeak  
  
ENTRYPOINT ["/opt/teamspeak/ts3server_minimal_runscript.sh"]  
  

