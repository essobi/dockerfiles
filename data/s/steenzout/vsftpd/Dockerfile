FROM alpine:latest  
MAINTAINER Pedro Salgado "steenzout@ymail.com"  
ONBUILD ARG FTP_USER  
ONBUILD ARG FTP_PASSWORD  
ONBUILD ARG FTP_HOME  
  
ONBUILD ENV FTP_USER ${FTP_USER}  
ONBUILD ENV FTP_PASSWORD ${FTP_PASSWORD}  
ONBUILD ENV FTP_HOME ${FTP_HOME}  
  
# installation  
RUN set -x \  
&& apk add --update vsftpd \  
&& rm -rf /var/cache/apk/* \  
&& mkdir -p /etc/vsftpd \  
&& mkdir -p /var/log/vsftpd \  
&& chown vsftp /var/log/vsftpd \  
&& ln -sf /dev/stdout /var/log/vsftpd/vsftpd.log \  
&& mkdir -p /var/lib/vsftpd/chroot  
  
# configuration  
ADD vsftpd.conf /etc/vsftpd/vsftpd.conf  
  
ONBUILD RUN adduser -D -h ${FTP_HOME} -s /bin/false ${FTP_USER} \  
&& echo "${FTP_USER}:$(echo ${FTP_PASSWORD} | mkpasswd -m SHA-512)" | chpasswd
-e \  
&& mkdir -p /etc/vsftpd/users \  
&& touch ${FTP_USER} /etc/vsftpd/users/${FTP_USER} \  
&& chown ${FTP_USER} /etc/vsftpd/users/${FTP_USER} \  
&& echo ${FTP_USER} > /etc/vsftpd/vsftpd.chroot_list  
  
VOLUME /etc/vsftpd  
VOLUME /var/log/vsftpd  
ONBUILD VOLUME "${FTP_HOME}"  
  
EXPOSE 20 21 10090-10100  
ENTRYPOINT ["/usr/sbin/vsftpd"]  
CMD ["/etc/vsftpd/vsftpd.conf"]  

