FROM alpine:3.4  
  
MAINTAINER avenus.pl  
  
ENV FTP_USER=foo \  
FTP_PASS=foo123 \  
PASV_ADDRESS=someadres.com \  
PASV_MIN=21100 \  
PASV_MAX=21110  
  
RUN \  
apk update && apk upgrade && apk \--update add \--no-cache vsftpd openssl \  
&& apk \--update add \--no-cache \--virtual .build-dependencies build-base
linux-pam-dev curl tar  
  
RUN echo "local_enable=YES" >> /etc/vsftpd/vsftpd.conf \  
&& echo "chroot_local_user=YES" >> /etc/vsftpd/vsftpd.conf \  
&& echo "allow_writeable_chroot=YES" >> /etc/vsftpd/vsftpd.conf \  
&& echo "background=NO" >> /etc/vsftpd/vsftpd.conf \  
&& echo "ftpd_banner=Welcome to FTP Server" >> /etc/vsftpd/vsftpd.conf \  
&& echo "dirmessage_enable=YES" >> /etc/vsftpd/vsftpd.conf \  
&& echo "max_clients=0" >> /etc/vsftpd/vsftpd.conf \  
&& echo "max_per_ip=0" >> /etc/vsftpd/vsftpd.conf \  
&& echo "write_enable=YES" >> /etc/vsftpd/vsftpd.conf \  
&& echo "virtual_use_local_privs=YES" >> /etc/vsftpd/vsftpd.conf \  
&& echo "guest_enable=YES" >> /etc/vsftpd/vsftpd.conf \  
&& echo "hide_ids=YES" >> /etc/vsftpd/vsftpd.conf \  
&& echo "pam_service_name=vsftpd_virtual" >> /etc/vsftpd/vsftpd.conf \  
&& echo "user_sub_token=\$USER" >> /etc/vsftpd/vsftpd.conf \  
&& echo "local_root=/home/vsftpd/\$USER" >> /etc/vsftpd/vsftpd.conf \  
&& echo "secure_chroot_dir=/var/run/vsftpd/empty" >> /etc/vsftpd/vsftpd.conf \  
&& echo "local_umask=022" >> /etc/vsftpd/vsftpd.conf \  
&& echo "passwd_chroot_enable=yes" >> /etc/vsftpd/vsftpd.conf \  
&& echo "pasv_enable=Yes" >> /etc/vsftpd/vsftpd.conf \  
&& echo "pasv_promiscuous=Yes" >> /etc/vsftpd/vsftpd.conf \  
&& echo "listen_ipv6=NO" >> /etc/vsftpd/vsftpd.conf \  
&& echo "nopriv_user=www-data" >> /etc/vsftpd/vsftpd.conf \  
&& echo "ftp_username=www-data" >> /etc/vsftpd/vsftpd.conf \  
&& echo "guest_username=www-data" >> /etc/vsftpd/vsftpd.conf \  
&& echo "chown_username=www-data" >> /etc/vsftpd/vsftpd.conf \  
&& echo "chown_uploads=YES" >> /etc/vsftpd/vsftpd.conf \  
&& echo "chown_upload_mode=0600" >> /etc/vsftpd/vsftpd.conf \  
&& echo "seccomp_sandbox=NO" >> /etc/vsftpd/vsftpd.conf \  
&& echo "user_config_dir=/conf/vsftpd/users_config" >> /etc/vsftpd/vsftpd.conf
\  
&& sed -i "s/anonymous_enable=YES/anonymous_enable=NO/"
/etc/vsftpd/vsftpd.conf  
  
  
  
COPY vsftpd_virtual /etc/pam.d/  
COPY vsftpd.sh /usr/sbin/  
  
RUN \  
mkdir /pam && \  
cd pam && \  
curl -sSL https://github.com/prapdm/libpam-pwdfile/archive/v1.0.tar.gz | tar
xz \--strip 1 && \  
make install && \  
cd .. && \  
rm -rvf pam && \  
mkdir -p /home/www-data && \  
#82 is the standard uid/gid for "www-data" in Alpine for php-fpm. Php need
write permision, so let's give them  
addgroup -g 82 -S www-data && \  
adduser -u 82 -S -D -G www-data -h /home/www-data -s /sbin/nologin www-data &&
\  
chown -R www-data:www-data /home/www-data && \  
mkdir -p /var/run/vsftpd/empty && \  
mkdir -p /home/vsftpd && \  
mkdir -p /conf/vsftpd && \  
mkdir -p /conf/vsftpd/users_config && \  
chown -R ftp:ftp /home/vsftpd && \  
echo "Delete Build pkgs" && \  
apk del .build-dependencies && \  
rm -rvf /var/cache/apk/* && \  
rm -rvf /tmp/* && \  
rm -rvf /src && \  
rm -rvf /var/log/*  
  
  
RUN chmod +x /usr/sbin/vsftpd.sh  
  
  
EXPOSE 21 21100-21110  
  
CMD /usr/sbin/vsftpd.sh  

