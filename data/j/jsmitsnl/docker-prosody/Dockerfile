FROM debian:stable  
  
MAINTAINER Johan Smits <johan@smitsmail.net>  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV __FLUSH_LOG yes  
  
RUN apt-get update && \  
apt-get install -y --no-install-recommends \  
gnupg2 \  
lua-bitop \  
lua-sec \  
lua-zlib \  
lua-dbi-sqlite3 \  
lua-dbi-mysql \  
lua-dbi-postgresql \  
lsb-release \  
sasl2-bin \  
lua-cyrussasl \  
libsasl2-modules \  
openssl \  
ca-certificates \  
supervisor \  
wget && \  
echo deb http://packages.prosody.im/debian $(lsb_release -sc) main | tee -a
/etc/apt/sources.list && \  
wget https://prosody.im/files/prosody-debian-packages.key -O- | apt-key add -
&& \  
apt-get update && \  
apt-get install -y --no-install-recommends prosody && \  
rm -rf /var/lib/apt/lists/* && \  
  
sed -i '/log = {/i \daemonize = false;' /etc/prosody/prosody.cfg.lua && \  
sed -i 's/--"compression";/"compression";/g' /etc/prosody/prosody.cfg.lua && \  
sed -i 's/-- "\\*console";/"*console";/g' /etc/prosody/prosody.cfg.lua && \  
sed -i 's/c2s_require_encryption = false/c2s_require_encryption = true/g'
/etc/prosody/prosody.cfg.lua && \  
sed -i 's/authentication = "internal_hashed"/authentication = "cyrus"/g'
/etc/prosody/prosody.cfg.lua && \  
mkdir /var/run/prosody && \  
chown prosody:prosody -Rf /etc/prosody /var/run/prosody  
  
COPY ./host_skel.cfg.lua /etc/prosody/conf.avail/  
  
COPY ./sasl_prosody.conf /etc/sasl/prosody.conf  
RUN adduser prosody sasl  
  
# Configure supervisor  
COPY ./supervisor/* /etc/supervisor/conf.d/  
  
COPY ./entrypoint.sh /entrypoint.sh  
RUN chmod 755 /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
  
EXPOSE 5222 5269  
  
CMD ["prosody"]  

