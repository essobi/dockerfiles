FROM alpine:3.6  
LABEL maintainer="Isaac A. <isaac@isaacs.site>" \  
contributor="Dimitri G. <dev@dmgnx.net>" \  
contributor="Antoine Mary <antoinee.mary@gmail.com>"  
  
### SET ENVIRONNEMENT  
ENV LANG="en_US.UTF-8"  
### SETUP  
COPY entrypoint.sh /entrypoint.sh  
RUN set -ex ; \  
apk add --no-cache --virtual .build-deps gcc make musl-dev ncurses-dev
openssl-dev readline-dev wget git ; \  
chmod +x /entrypoint.sh  
  
# Fetch sources  
RUN git clone https://github.com/SoftEtherVPN/SoftEtherVPN_Stable  
  
# Compile and Install  
RUN cd SoftEtherVPN_Stable ; \  
cp src/makefiles/linux_64bit.mak Makefile ; \  
make ; make install ; make clean  
  
# Stripping vpnserver  
RUN strip /usr/vpnserver/vpnserver ; \  
mkdir -p /etc/vpnserver /var/log/vpnserver; ln -s
/etc/vpnserver/vpn_server.config /usr/vpnserver/vpn_server.config  
  
# Cleaning  
RUN apk del .build-deps  
  
# Reintroduce necessary libraries  
RUN apk add --no-cache --virtual .run-deps libcap libcrypto1.0 libssl1.0
ncurses-libs readline su-exec  
  
# Remove vpnbridge, vpnclient, vpncmd, and build files  
RUN cd .. ; rm -rf /usr/vpnbridge /usr/bin/vpnbridge /usr/vpnclient
/usr/bin/vpnclient /usr/vpncmd /usr/bin/vpncmd /usr/bin/vpnserver
SoftEtherVPN_Stable  
  
EXPOSE 443/tcp 992/tcp 1194/udp 5555/tcp  
  
VOLUME ["/etc/vpnserver", "/var/log/vpnserver"]  
  
ENTRYPOINT ["/bin/ash"]  
CMD ["/usr/vpnserver/vpnserver", "start"]  

