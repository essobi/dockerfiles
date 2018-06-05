FROM alpine:latest  
  
ENV UID 1000  
ENV USERNAME samba  
ENV GID 1000  
ENV GROUP samba  
ENV PASSWORD password  
ENV S6_VERSION 1.18.1.5  
#Download s6-overlay's files  
ADD https://keybase.io/justcontainers/key.asc /tmp/key.asc  
ADD https://github.com/just-
containers/s6-overlay/releases/download/v$S6_VERSION/s6-overlay-amd64.tar.gz
/tmp/s6.tar.gz  
ADD https://github.com/just-
containers/s6-overlay/releases/download/v$S6_VERSION/s6-overlay-
amd64.tar.gz.sig /tmp/s6.sig  
  
#COPY repositories /etc/apk/repositories  
#curl is no longer needed  
RUN set -xe\  
&& apk add --update --no-cache samba-common-tools samba-server gnupg  
  
#Verify s6-overlay' signature and untar  
RUN set -xe \  
&& cd /tmp \  
&& gpg --import /tmp/key.asc \  
&& gpg --verify /tmp/s6.sig /tmp/s6.tar.gz \  
&& tar xzf s6.tar.gz -C / \  
&& rm -rf /tmp /root/.gnupg  
  
RUN set -xe \  
&& apk del gnupg  
  
COPY create-samba-users.s6 /etc/cont-init.d/00-create-samba-users.sh  
COPY create-tmp-folder.s6 /etc/cont-init.d/01-create-tmp-folder.sh  
#COPY create-nobody-user.s6 /etc/cont-init.d/02-create-nobody-user.sh  
COPY run-samba-server.s6 /etc/services.d/samba/run  
#COPY finish-samba-server.s6 /etc/services.d/samba/finish  
EXPOSE 137/udp 138/udp 139/tcp 445/tcp  
  
VOLUME ["/config", "/shared"]  
  
CMD ["/init"]  

