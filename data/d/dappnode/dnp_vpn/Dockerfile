FROM node:alpine as build  
  
WORKDIR /usr/src/app  
  
RUN apk add --update --no-cache \  
build-base  
  
COPY src .  
  
RUN npm install  
  
FROM alpine  
  
WORKDIR /usr/src/app  
  
COPY \--from=build /usr/local/bin/node /usr/local/bin/node  
COPY \--from=build /usr/src/app /usr/src/app  
  
RUN apk add --update --no-cache \  
libreswan \  
ppp \  
xl2tpd \  
openssl \  
openrc \  
bind-tools \  
# gettext package contains envsubst, template engine for the VPN files  
gettext \  
supervisor \  
&& rc-status \  
&& touch /run/openrc/softlevel \  
&& rc-update add ipsec \  
&& ALPINE_GLIBC_BASE_URL="https://github.com/sgerrand/alpine-pkg-
glibc/releases/download" && \  
ALPINE_GLIBC_PACKAGE_VERSION="2.27-r0" && \  
ALPINE_GLIBC_BASE_PACKAGE_FILENAME="glibc-$ALPINE_GLIBC_PACKAGE_VERSION.apk"
&& \  
ALPINE_GLIBC_BIN_PACKAGE_FILENAME="glibc-
bin-$ALPINE_GLIBC_PACKAGE_VERSION.apk" && \  
ALPINE_GLIBC_I18N_PACKAGE_FILENAME="glibc-i18n-$ALPINE_GLIBC_PACKAGE_VERSION.apk"
&& \  
apk add --no-cache --virtual=.build-dependencies wget ca-certificates && \  
wget \  
"https://raw.githubusercontent.com/sgerrand/alpine-pkg-
glibc/master/sgerrand.rsa.pub" \  
-O "/etc/apk/keys/sgerrand.rsa.pub" && \  
wget \  
"$ALPINE_GLIBC_BASE_URL/$ALPINE_GLIBC_PACKAGE_VERSION/$ALPINE_GLIBC_BASE_PACKAGE_FILENAME"
\  
"$ALPINE_GLIBC_BASE_URL/$ALPINE_GLIBC_PACKAGE_VERSION/$ALPINE_GLIBC_BIN_PACKAGE_FILENAME"
\  
"$ALPINE_GLIBC_BASE_URL/$ALPINE_GLIBC_PACKAGE_VERSION/$ALPINE_GLIBC_I18N_PACKAGE_FILENAME"
&& \  
apk add --no-cache \  
"$ALPINE_GLIBC_BASE_PACKAGE_FILENAME" \  
"$ALPINE_GLIBC_BIN_PACKAGE_FILENAME" \  
"$ALPINE_GLIBC_I18N_PACKAGE_FILENAME" && \  
\  
rm "/etc/apk/keys/sgerrand.rsa.pub" && \  
/usr/glibc-compat/bin/localedef --force --inputfile POSIX --charmap UTF-8
"$LANG" || true && \  
echo "export LANG=$LANG" > /etc/profile.d/locale.sh && \  
\  
apk del glibc-i18n && \  
\  
rm "/root/.wget-hsts" && \  
apk del .build-dependencies && \  
rm \  
"$ALPINE_GLIBC_BASE_PACKAGE_FILENAME" \  
"$ALPINE_GLIBC_BIN_PACKAGE_FILENAME" \  
"$ALPINE_GLIBC_I18N_PACKAGE_FILENAME"  
  
# Copying source contents:  
# - supervisord.conf  
# - ipsec  
# - VPN setup shell: init.sh, templates/  
# - node files: package.json, client.js  
COPY src/ipsec /etc/init.d/ipsec  
  
RUN chmod 755 init.sh  
  
RUN mkdir -p /usr/src/app/secrets  
# envs for init.sh -> node communication  
ENV CREDENTIALS_FILE_PATH /etc/ppp/chap-secrets  
ENV VPN_IP_FILE_PATH /usr/src/app/secrets/server-ip  
ENV VPN_PSK_FILE_PATH /usr/src/app/secrets/server-psk  
ENV VPN_NAME_FILE_PATH /etc/vpnname  
ENV VPN_ADMIN_PASS_FILE_PATH /usr/src/app/secrets/admin-pass  
ENV VPN_DNS_SRV1 172.33.1.2  
ENV VPN_DNS_SRV2 8.8.8.8  
# location of the OTP parsing tool  
ENV DAPPNODE_OTP_URL https://dappnode.github.io/DAppNode_OTP/  
  
RUN ln -s /usr/src/app/getAdminCredentials.js /usr/bin/getAdminCredentials  
RUN chmod +x /usr/src/app/getAdminCredentials.js  
  
# Supervisord processes:  
# > /usr/src/app/init.sh (libreswan VPN, executes xl2tpd)  
# > node client.js (VPN user managment API)  
CMD ["supervisord"]  

