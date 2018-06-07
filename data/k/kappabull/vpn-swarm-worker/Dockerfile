FROM docker:1.12.2-rc3  
MAINTAINER kappabull <kappa8v11@gmail.com>  
  
EXPOSE 443 992 5555  
# VPN各種設定項目 (基本的にはServerの値と合わせる)  
ENV ACCOUNT=private  
ENV NICNAME=vlan  
ENV SERVER="0.0.0.0:5555"  
ENV HUBNAME=DEFAULT  
ENV USERNAME=user  
ENV USERPASS=something  
# Swarm設定項目  
ENV SWARM_MANAGER_ADDRESS \  
SWARM_MANAGER_PORT  
ENV LANG=en_US.UTF-8  
ARG BUILD_PKG="tar gcc git curl expat libssh2 pcre libc-dev readline-dev zlib-
dev openssl-dev ncurses-dev make"  
ARG TEMP_DIR="/tmp/softethervpn"  
ARG VERSION=4.22-9634-beta  
  
LABEL description="SoftEtherVPN Server"  
LABEL version="${VERSION}"  
  
RUN set -e \  
&& apk add --no-cache ${BUILD_PKG} iptables iproute2 readline ncurses zlib
dhclient \  
&& mkdir -p ${TEMP_DIR} \  
&& git clone \--branch "v${VERSION}" \--depth 1
https://github.com/SoftEtherVPN/SoftEtherVPN.git ${TEMP_DIR} \  
&& cd ${TEMP_DIR} \  
&& cp src/makefiles/linux_64bit.mak Makefile \  
&& make \  
&& make install \  
&& cd \- \  
&& apk del --purge ${BUILD_PKG} \  
&& rm -rf /var/cache/apk/* ${TEMP_DIR}  
  
ADD entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh  
ENTRYPOINT ["/bin/sh", "/entrypoint.sh"]

