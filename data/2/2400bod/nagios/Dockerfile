FROM alpine  
  
MAINTAINER 2400bod <bod@gri.kiev.ua>  
  
#-----------------------------------------------------------  
# Settings  
  
ENV TZ='UTC' \  
\  
NAGIOSADMIN='nagiosadmin' \  
NAGIOSPASSWORD='nagios' \  
\  
NAGIOS_USER='nagios' \  
NAGIOS_GROUP='nagios' \  
\  
HOST_USER_ID='1000' \  
HOST_GROUP_ID='1000'  
#-----------------------------------------------------------  
  
ENV PKGS="busybox arping nagios nagios-web lighttpd lighttpd-mod_auth
apache2-utils fcgi php5-cgi php5-xml openssl postfix" \  
BPKGS="git tzdata alpine-sdk openssl-dev"  
  
RUN addgroup -g ${HOST_GROUP_ID} ${NAGIOS_GROUP} && \  
adduser -h /var/nagios -s /sbin/nologin -G ${NAGIOS_GROUP} -D -u
${HOST_USER_ID} ${NAGIOS_USER} && \  
apk upgrade --update && \  
apk --no-cache add $PKGS && \  
apk --no-cache add --virtual .build $BPKGS && \  
apk search nagios-plugins | sed -r 's/-\d.+$//' | xargs apk --no-cache add &&
\  
sed -ri "s/^nagios_user=(.+)$/nagios_user=${NAGIOS_USER}/"
/etc/nagios/nagios.cfg && \  
sed -ri "s/^nagios_group=(.+)$/nagios_group=${NAGIOS_GROUP}/"
/etc/nagios/nagios.cfg && \  
echo "use_timezone=$TZ" >> /etc/nagios/nagios.cfg && \  
echo $TZ > /etc/TZ && \  
cp /usr/share/zoneinfo/$TZ /etc/localtime && \  
sed -ri 's,/var/www/localhost,/usr/share/nagios,' /etc/lighttpd/lighttpd.conf
&& \  
sed -ri 's/^#(\s+include "mod_fastcgi.conf")/\1/' /etc/lighttpd/lighttpd.conf
&& \  
echo 'include "nagios.conf"' >> /etc/lighttpd/lighttpd.conf && \  
sed -ri s,/nagios/cgi-bin,/cgi-bin, /usr/share/nagios/htdocs/config.inc.php &&
\  
mkdir -p /run/lighttpd && \  
chown lighttpd:lighttpd /run/lighttpd && \  
addgroup lighttpd nagios && \  
cp -R /etc/nagios /etc/nagios.orig && \  
cp -R /var/nagios /var/nagios.orig && \  
chmod u+s /bin/ping && \  
cd /tmp && \  
git clone https://anonscm.debian.org/git/pkg-nagios/pkg-nagios-images.git
logos && \  
for d in $(find . -mindepth 2 -maxdepth 2 -type d -a ! -name debian -a ! -name
.git); do mv $d /usr/share/nagios/htdocs/images/logos; done && \  
git clone https://github.com/NagiosEnterprises/nrpe.git nrpe && \  
cd /tmp/nrpe && \  
./configure --with-nagios-user=${NAGIOS_USER} --with-nagios-
group=${NAGIOS_GROUP} --prefix=/usr/lib/nagios --with-
pluginsdir=/usr/lib/nagios/plugins --enable-ssl && \  
make check_nrpe && make install-plugin && \  
apk del .build && \  
rm -rf /var/cache/apk/* /tmp/* /core  
  
#-----------------------------------------------------------  
  
ADD lighttpd_nagios.conf /etc/lighttpd/nagios.conf  
ADD bin/* /bin/  
  
EXPOSE 80  
  
VOLUME /etc/nagios /var/nagios  
  
CMD /bin/start_nagios.sh  
  
#-----------------------------------------------------------  

