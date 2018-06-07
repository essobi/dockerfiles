FROM alpine:3.6  
MAINTAINER Emil Lerch  
  
RUN apk add --no-cache apache2-webdav apache2-utils \  
&& mkdir /dav \  
&& chmod 770 /dav \  
&& chown root:www-data /dav \  
&& sed -i 's#Alias /uploads#Alias /#g' /etc/apache2/conf.d/dav.conf \  
&& sed -i 's#/usr/uploads#/dav/#g' /etc/apache2/conf.d/dav.conf \  
&& sed -i 's#DAV-upload#dav#' /etc/apache2/conf.d/dav.conf \  
&& sed -i 's/Require method/#Require method/' /etc/apache2/conf.d/dav.conf \  
&& sed -i 's/Require user admin/Require valid-user/'
/etc/apache2/conf.d/dav.conf \  
&& echo TransferLog /dev/stdout >> /etc/apache2/httpd.conf \  
&& echo ErrorLog /dev/stderr >> /etc/apache2/httpd.conf \  
&& echo 'ServerName ${VIRTUAL_HOST}' >> /etc/apache2/httpd.conf \  
&& mkdir -p /run/apache2 \  
&& mkdir -p /var/lib/dav \  
&& chown root:www-data /var/lib/dav \  
&& chmod 770 /var/lib/dav \  
&& echo $'#!/bin/sh \n\  
#htpasswd -cb /usr/user.password $USERNAME $PASSWORD \n\  
(echo -n "$USERNAME:dav:" && echo -n "$USERNAME:dav:$PASSWORD" | md5sum | awk
\\{print\ \$1\\} ) > /usr/user.passwd \n\  
chown root:www-data /usr/user.passwd \n\  
chmod 640 /usr/user.passwd \n\  
\n\  
/usr/sbin/httpd -d /etc/apache2 -f /etc/apache2/httpd.conf -DFOREGROUND -e
info \n\  
' > /run.sh \  
&& chmod 755 /run.sh  
  
VOLUME ["/dav"]  
EXPOSE 80  
  
CMD ["/run.sh"]

