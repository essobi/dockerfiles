# BASE bussybox  
FROM cesanta/docker_auth:stable  
  
# install openssl for REGISTRY_AUTH_TOKEN_ROOTCERTBUNDLE  
ADD ./rootfs.tar /  
ADD ./opkg.conf /etc/opkg.conf  
ADD ./opkg-install /usr/bin/opkg-install  
ADD ./functions.sh /lib/functions.sh  
RUN opkg-cl install
http://downloads.openwrt.org/snapshots/trunk/x86/64/packages/base/libgcc_5.3.0-1_x86_64.ipk  
RUN opkg-cl install
http://downloads.openwrt.org/snapshots/trunk/x86/64/packages/base/libc_1.1.16-1_x86_64.ipk  
  
RUN opkg-install openssl-util  
  
ENV AUTH_SERVER "/docker_auth/auth_server"  
ENV AUTH_CONFIG "/config/auth_config.yml"  
ENV COMMON_NAME ""  
COPY entrypoint.sh /  
ENTRYPOINT [ "/entrypoint.sh" ]  

