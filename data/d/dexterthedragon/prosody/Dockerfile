################################################################################  
# Build a dockerfile for Prosody XMPP server  
# Based on ubuntu  
################################################################################  
  
FROM ubuntu:14.04  
  
MAINTAINER Lloyd Watkin <lloyd@evilprofessor.co.uk>  
  
RUN apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y wget \  
&& rm -rf /var/lib/apt/lists/* \  
&& wget https://prosody.im/files/prosody-debian-packages.key -O- | sudo apt-
key add - \  
&& DEBIAN_FRONTEND=noninteractive apt-get purge -y --auto-remove wget \  
&& echo deb http://packages.prosody.im/debian $(lsb_release -sc) main >
/etc/apt/sources.list.d/prosody.list  
  
ENV PROSODY_VERSION 0.9.7  
  
# Install and configure prosody  
RUN apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \  
prosody=$PROSODY_VERSION* \  
lua-dbi-mysql \  
lua-dbi-postgresql \  
lua-dbi-sqlite3 \  
lua-event \  
lua-sec \  
lua-zlib \  
&& rm -rf /var/lib/apt/lists/* \  
&& sed -i '1s/^/daemonize = false;\n/' /etc/prosody/prosody.cfg.lua \  
&& perl -i -pe 'BEGIN{undef $/;} s/^log = {.*?^}$/log = {\n {levels = {min =
"info"}, to = "console"};\n}/smg' /etc/prosody/prosody.cfg.lua  
  
COPY ./entrypoint.sh /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
  
EXPOSE 80 443 5222 5269 5347 5280 5281  
CMD ["prosodyctl", "start"]  

