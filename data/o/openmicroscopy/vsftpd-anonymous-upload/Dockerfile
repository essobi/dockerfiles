#  
# Dockerfile for vsftpd  
#  
  
FROM alpine:3.7  
MAINTAINER ome-devel@lists.openmicroscopy.org.uk  
  
RUN set -xe \  
&& apk add -U vsftpd \  
&& passwd -l root \  
&& rm -rf /var/cache/apk/*  
  
ADD vsftpd.conf vsftpd.email_passwords vsftpd.banner /etc/vsftpd/  
RUN ln -s /etc/vsftpd/vsftpd.email_passwords /etc/vsftpd.email_passwords  
# Log to docker stdout (vsftpd must be run as PID 1)  
RUN ln -sf /proc/1/fd/1 /var/log/vsftpd.log  
  
RUN install -d -m u+wx,u-r,g+rwxs,o-rwx -o ftp -g root /var/lib/ftp/incoming  
VOLUME /var/lib/ftp/incoming  
WORKDIR /var/lib/ftp  
  
EXPOSE 21 32022-32041  
  
CMD ["vsftpd", "/etc/vsftpd/vsftpd.conf"]  

