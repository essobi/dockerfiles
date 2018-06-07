FROM alpine:3.5  
LABEL description "PostfixAdmin is a web based interface used to manage
mailboxes" \  
maintainer="Hardware <contact@meshup.net>"  
  
ARG VERSION=3.0.2  
# https://pgp.mit.edu/pks/lookup?search=0xEB7EB945&fingerprint=on&op=index  
# pub 4096R/EB7EB945 2012-01-25 David Goodwin (PalePurple)
<david@palepurple.co.uk>  
ARG GPG_SHORTID="0xEB7EB945"  
ARG GPG_FINGERPRINT="2D83 3163 D69B B8F6 BFEF 179D 4ECC 3566 EB7E B945"  
ENV GID=991 \  
UID=991 \  
DBTYPE=mysqli \  
DBHOST=mariadb \  
DBUSER=postfix \  
DBNAME=postfix \  
SMTPHOST=mailserver  
  
RUN echo "@community https://nl.alpinelinux.org/alpine/v3.5/community" >>
/etc/apk/repositories \  
&& BUILD_DEPS=" \  
ca-certificates \  
gnupg" \  
&& apk -U add \  
${BUILD_DEPS} \  
nginx \  
s6 \  
git \  
su-exec \  
dovecot \  
php7-fpm@community \  
php7-imap@community \  
php7-mysqli@community \  
php7-session@community \  
php7-mbstring@community \  
&& git clone https://github.com/AnthoDingo/postfixadmin.git /postfixadmin \  
&& apk del ${BUILD_DEPS} \  
&& rm -rf /var/cache/apk/* /tmp/* /root/.gnupg  
  
COPY nginx.conf /etc/nginx/nginx.conf  
COPY php-fpm.conf /etc/php7/php-fpm.conf  
COPY setup /usr/local/bin/setup  
COPY s6.d /etc/s6.d  
COPY run.sh /usr/local/bin/run.sh  
  
RUN chmod +x /usr/local/bin/* /etc/s6.d/*/* /etc/s6.d/.s6-svscan/*  
  
EXPOSE 8888  
CMD ["run.sh"]  

