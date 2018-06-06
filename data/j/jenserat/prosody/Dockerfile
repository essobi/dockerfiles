FROM debian:jessie  
MAINTAINER Jens Erat <email@jenserat.de>  
  
# Remove SUID programs  
RUN for i in `find / -perm +6000 -type f 2>/dev/null`; do chmod a-s $i; done  
  
VOLUME /etc/prosody  
VOLUME /var/lib/prosody  
  
# 5000/tcp: mod_proxy65  
# 5222/tcp: client to server  
# 5223/tcp: deprecated, SSL client to server  
# 5269/tcp: server to server  
# 5280/tcp: BOSH  
# 5281/tcp: Secure BOSH  
# 5347/tcp: XMPP component  
EXPOSE 5000 5222 5223 5269 5280 5281 5347  
ENV PROSODY_VERSION 0.9.12-1~jessie1  
  
COPY 107D65A0A148C237FDF00AB47393D7E674D9DBB5.gpg /root  
  
RUN apt-key add /root/107D65A0A148C237FDF00AB47393D7E674D9DBB5.gpg && \  
echo deb http://packages.prosody.im/debian jessie main >>/etc/apt/sources.list
&& \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-suggests
prosody=${PROSODY_VERSION} curl lua-sec lua-event lua-zlib lua-ldap lua-dbi-
mysql lua-dbi-postgresql lua-dbi-sqlite3 && \  
mkdir /opt/prosody-modules && \  
curl https://hg.prosody.im/prosody-modules/archive/tip.tar.gz | tar xz -C
/opt/prosody-modules --strip-components=1 && \  
apt-get purge --auto-remove -y curl && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
USER prosody  
CMD ["/usr/bin/prosodyctl", "start"]  

