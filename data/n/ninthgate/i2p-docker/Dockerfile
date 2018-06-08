FROM debian:jessie  
  
MAINTAINER dzirtt  
  
#ENV I2P_VERSION 0.9.23-1~deb8u+1  
ENV I2P_DIR /usr/share/i2p  
ENV DEBIAN_FRONTEND noninteractive  
  
#set here user:group from what start service inside container  
ENV USER i2psvc  
ENV GROUP i2psvc  
  
RUN echo "deb http://deb.i2p2.no/ jessie main" >
/etc/apt/sources.list.d/i2p.list  
  
RUN apt-key adv --keyserver hkp://pool.sks-keyservers.net --recv-key
0x67ECE5605BCF1346 && \  
apt-get update && \  
apt-get -y install --no-install-recommends i2p locales wget nano curl && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /var/tmp/* /tmp/*  
  
ENV GOSU_VERSION 1.7  
RUN set -x \  
&& wget -O /usr/local/bin/gosu
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg
--print-architecture)" \  
&& wget -O /usr/local/bin/gosu.asc
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg
--print-architecture).asc" \  
&& export GNUPGHOME="$(mktemp -d)" \  
&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
0xB42F6819007F00F88E364FD4036A9C25BF357DD4 \  
&& gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu \  
&& rm -r "$GNUPGHOME" /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu \  
&& gosu nobody true  
  
RUN rm -rf /var/lib/i2p/* && \  
chown -R $USER:$GROUP /var/lib/i2p && \  
chmod 700 -R /var/lib/i2p  
  
# Enable UTF-8, mostly for I2PSnark  
RUN sed -i 's/.*\\(en_US\\.UTF-8\\)/\1/' /etc/locale.gen && \  
/usr/sbin/locale-gen && \  
/usr/sbin/update-locale LANG=en_US.UTF-8 LANGUAGE="en_US:en"  
  
RUN sed -i 's/127\\.0\\.0\\.1/0.0.0.0/g' ${I2P_DIR}/i2ptunnel.config && \  
sed -i 's/::1,127\\.0\\.0\\.1/0.0.0.0/g' ${I2P_DIR}/clients.config && \  
printf "i2cp.tcp.bindAllInterfaces=true\n" >> ${I2P_DIR}/router.config && \  
printf "i2np.ipv4.firewalled=true\n" >> ${I2P_DIR}/router.config && \  
printf "i2np.ntcp.ipv6=false\n" >> ${I2P_DIR}/router.config && \  
printf "i2np.udp.ipv6=false\n" >> ${I2P_DIR}/router.config && \  
printf "i2np.upnp.enable=false\n" >> ${I2P_DIR}/router.config && \  
printf "logger.minimumOnScreenLevel=WARN\n" >> ${I2P_DIR}/logger.config && \  
printf "logger.defaultLevel=INFO\n" >> ${I2P_DIR}/logger.config  
  
##  
# Expose some ports used by I2P  
# Description at https://geti2p.net/ports  
#  
# Main ports:  
# 4444 — HTTP proxy  
# 6668 — Proxy to Irc2P  
# 7657 — router console  
# 7658 — self-hosted eepsite  
# 7659 — SMTP proxy to smtp.postman.i2p  
# 7660 — POP3 proxy to pop.postman.i2p  
# 8998 — Proxy to mtn.i2p-projekt.i2p  
##  
EXPOSE 4444 7657 6668 7659 7660  
#for persistence run with VOLUME uncomment or -v /youPath:/var/lib/i2p  
#VOLUME /var/lib/i2p  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
  
ADD docker-entrypoint.sh /  
RUN chmod +x /docker-entrypoint.sh  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["i2prouter", "console"]  

