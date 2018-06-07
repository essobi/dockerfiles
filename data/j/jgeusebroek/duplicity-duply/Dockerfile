FROM alpine:3.7  
MAINTAINER Jeroen Geusebroek <me@jeroengeusebroek.nl>  
  
ENV PACKAGE_LIST="duplicity duply gnupg py-paramiko py2-pip py-pexpect py-
requests py-requests-oauthlib rsync openssh-client lftp bash pwgen ca-
certificates mariadb-client mc" \  
LANG='en_US.UTF-8' \  
LANGUAGE='en_US.UTF-8' \  
TIMEZONE='Europe/Amsterdam' \  
REFRESHED_AT='2017-12-08' \  
\  
KEY_TYPE='RSA' \  
KEY_LENGTH='2048' \  
SUBKEY_TYPE='RSA' \  
SUBKEY_LENGTH='2048' \  
NAME_REAL='Duply backup' \  
NAME_EMAIL='duply@localhost' \  
PASSPHRASE='random' \  
\  
GPG_TTY='/dev/console'  
RUN apk add \--no-cache ${PACKAGE_LIST} && \  
pip install fasteners  
  
VOLUME [ "/root" ]  
  
COPY files/ssh/config /root/.ssh/config  
COPY files/entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["/bin/bash"]  

