FROM debian:latest  
MAINTAINER Vladimir Osintsev <oc@co.ru>  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN echo deb http://packages.prosody.im/debian stable main >>
/etc/apt/sources.list && \  
apt-key adv --keyserver pgp.mit.edu --recv-keys 7393D7E674D9DBB5 && \  
apt-get update && apt-get -y install --no-install-recommends \  
lua-event \  
lua-zlib \  
lua-dbi-mysql \  
lua-dbi-postgresql \  
lua-dbi-sqlite3 \  
lua-sec \  
prosody && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN ln -sf /dev/stdout /var/log/prosody/prosody.log && \  
ln -sf /dev/stderr /var/log/prosody/prosody.err && \  
chown -R prosody.prosody /var/log/prosody && \  
sed -ri \  
-e '1s/^/daemonize = false;\n/' \  
-e '/^--use_libevent /c use_libevent = true;' \  
/etc/prosody/prosody.cfg.lua  
  
VOLUME ["/etc/prosody", "/var/lib/prosody"]  
  
# Exposed ports:  
#  
# 5000/tcp: mod_proxy65  
# 5222/tcp: c2s  
# 5223/tcp: deprecated, c2s  
# 5269/tcp: s2s  
# 5280/tcp: BOSH  
# 5281/tcp: Secure BOSH  
# 5347/tcp: XMPP component  
#  
EXPOSE 5222 5269 5347 5280 5281  
USER prosody  
CMD ["prosodyctl", "start"]  

