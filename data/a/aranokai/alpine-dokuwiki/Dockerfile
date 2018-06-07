# Simple to use and highly versatile Open Source wiki software on lighttpd
server  
# This Dockerfile based on mprasil/dokuwiki & bambucha/dokuwiki  
# Usage:  
# Start: docker run [-d] -p 80:80 [--name dokuwiki] aranokai/ubuntu-dokuwiki  
# Backup: docker run --rm --volumes-from dokuwiki -v <backup_dir>:/backup
aranokai/ubuntu-dokuwiki tar czf /backup/<backup_name>.tgz /dokuwiki  
# Restore: docker run --rm --volumes-from dokuwiki -v <backup_dir>:/backup
aranokai/ubuntu-dokuwiki tar xzf /backup/<backup_name>.tgz  
FROM alpine:3.3  
MAINTAINER Arano-kai <captcha.is.evil@gmail.com>  
  
# Update -> install packages -> cleanup  
RUN apk --update add lighttpd php-cgi php-gd php-xml php-zlib php-zip php-
openssl ca-certificates && \  
rm -rf /var/cache/apk/*  
  
# Fix PHP FastCGI security issue  
RUN sed -i -e "s/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/g" /etc/php/php.ini  
  
# Configure lighttpd  
ADD dokuwiki.conf /etc/lighttpd/dokuwiki.conf  
RUN echo 'include "/etc/lighttpd/dokuwiki.conf"' >>
/etc/lighttpd/lighttpd.conf  
RUN mkdir /var/run/lighttpd \  
&& chown lighttpd:lighttpd /var/run/lighttpd  
  
# Path & name for downloaded archive  
ENV DOKUWIKI_ARH "/dokuwiki.tgz"  
# Set the version you want of Dokuwiki  
ENV DOKUWIKI_VERSION=2017-02-19d \  
DOKUWIKI_MD5=7fe22637eb32ca0feeb34ffb0bd524a4  
  
# Download link  
ENV DOKUWIKI_LNK
"http://download.dokuwiki.org/src/dokuwiki/dokuwiki-${DOKUWIKI_VERSION}.tgz"  
# Download Dokuviki -> check integrity -> deploy -> cleanup  
RUN wget -q -O "${DOKUWIKI_ARH}" "${DOKUWIKI_LNK}" \  
&& DOKUWIKI_MD5_OUT="$(md5sum ${DOKUWIKI_ARH} | awk '{print($1)}')" \  
&& if [ "${DOKUWIKI_MD5}" = "${DOKUWIKI_MD5_OUT}" ]; then \  
tar -zxf "${DOKUWIKI_ARH}" \  
&& mv /dokuwiki-"${DOKUWIKI_VERSION}" /dokuwiki \  
&& rm dokuwiki.tgz; \  
else \  
>&2 printf '\n\t\t\t%s\n' "$(basename -- ${DOKUWIKI_ARH})"; \  
>&2 printf '%s:\t%s\n' "Downloaded" "${DOKUWIKI_MD5_OUT}" \  
"Expected" "${DOKUWIKI_MD5}"; \  
>&2 printf '\n%s\n' 'Please, re-run build or check corresponding vars.'; \  
exit 1; \  
fi  
  
EXPOSE 80  
VOLUME
["/dokuwiki/data/","/dokuwiki/lib/plugins/","/dokuwiki/conf/","/dokuwiki/lib/tpl/","/var/log/lighttpd"]  
  
# Run lighttpd and cache clean loop  
CMD (while true; do find /dokuwiki/cache/ -type f -mtime +10 -delete; sleep
1d; done) 1>/dev/null 2>&1 & chown -R lighttpd:lighttpd /dokuwiki && chown -R
lighttpd:lighttpd /var/log/lighttpd && chmod 755 /dokuwiki &&
/usr/sbin/lighttpd -D -f /etc/lighttpd/lighttpd.conf  

