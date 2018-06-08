FROM ubuntu:16.04  
  
MAINTAINER clebeaupin <clebeaupin@noop.fr>  
  
RUN set -ex \  
&& apt-get update \  
&& apt-get install -y vsftpd libpam-pwdfile apache2-utils \  
&& rm /etc/vsftpd.conf \  
&& rm /etc/pam.d/vsftpd  
  
RUN mkdir -p /var/lib/ftp /etc/vsftpd/users /var/run/vsftpd \  
&& chown ftp:ftp /var/lib/ftp -R  
  
COPY vsftpd-entrypoint.sh /entrypoint.sh  
COPY vsftpd-pam.default /etc/pam.d/vsftpd  
COPY vsftpd.conf.default /templates/etc/vsftpd/vsftpd.conf  
COPY vsftpd-user-admin.default /templates/etc/vsftpd/users/admin  
  
RUN chmod +x /entrypoint.sh  
  
VOLUME /var/lib/ftp  
WORKDIR /var/lib/ftp  
  
EXPOSE 21  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD [ "vsftpd", "/etc/vsftpd/vsftpd.conf" ]  

