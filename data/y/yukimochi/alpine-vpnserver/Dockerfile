FROM alpine  
  
ARG VPN_VERSION=v4.27-9666  
ARG PKG_VERSION=v4.27-9666-beta  
ARG TREE_VERSION=v4.27-9666-beta-2018.04.21-tree  
  
ENV LANG=en_US.UTF-8  
RUN apk add -U --no-cache ca-certificates iptables ncurses openssl readline \  
&& apk add --no-cache --virt .dep build-base readline-dev openssl-dev ncurses-
dev \  
&& update-ca-certificates \  
&& wget http://jp.softether-
download.com/files/softether/${TREE_VERSION}/Source_Code/softether-
src-${PKG_VERSION}.tar.gz \  
&& tar fx softether-src-${PKG_VERSION}.tar.gz \  
&& rm softether-src-${PKG_VERSION}.tar.gz \  
&& cd ${VPN_VERSION}\  
&& sed -i -e
"s/#define\tBUILDER_NAME.*/#define\tBUILDER_NAME\t\t\"YUKIMOCHI\"\r/" -e
"s/#define\tBUILD_PLACE.*/#define\tBUILD_PLACE\t\t\"DockerHub\"\r/"
src/Cedar/Cedar.h \  
&& ./configure \  
&& make -j \  
&& make install \  
&& cd / \  
&& rm -rf ${VPN_VERSION} \  
&& apk del --purge .dep \  
&& rm -rf /tmp/* /var/cache/apk/*  
  
RUN cd /usr/vpnserver/ \  
&& mkdir -p logs/packet_log logs/security_log logs/server_log \  
&& ln -s /usr/vpnserver/logs/packet_log /usr/vpnserver/packet_log \  
&& ln -s /usr/vpnserver/logs/security_log /usr/vpnserver/security_log \  
&& ln -s /usr/vpnserver/logs/server_log /usr/vpnserver/server_log  
  
EXPOSE 443/tcp 992/tcp 1194/tcp 1194/udp 5555/tcp 500/udp 4500/udp  
VOLUME [ "/usr/vpnserver/logs", "/usr/vpnserver/vpn_server.config" ]  
CMD [ "/usr/vpnserver/vpnserver", "execsvc" ]  

