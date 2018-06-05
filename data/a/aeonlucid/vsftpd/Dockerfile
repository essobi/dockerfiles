FROM centos:7  
MAINTAINER Fer Uria <fauria@gmail.com>  
LABEL Description="vsftpd Docker image based on Centos 7. Supports passive
mode and virtual users." \  
License="Apache License 2.0" \  
Usage="docker run -d -p [HOST PORT NUMBER]:21 -v [HOST FTP HOME]:/home/vsftpd
fauria/vsftpd" \  
Version="1.0"  
  
# Configure user nobody to match unRAID's settings  
RUN \  
usermod -u 99 nobody && \  
usermod -g 100 nobody && \  
usermod -d /home nobody && \  
chown -R nobody:users /home  
  
RUN yum -y update && yum clean all  
RUN yum -y install httpd && yum clean all  
RUN yum install -y \  
vsftpd \  
db4-utils \  
db4 \  
iproute && yum clean all  
  
ENV FTP_PORT_DATA 20  
ENV FTP_PORT 21  
ENV FTP_USER admin  
ENV FTP_PASS **Random**  
ENV PASV_ADDRESS **IPv4**  
ENV PASV_MIN_PORT 21100  
ENV PASV_MAX_PORT 21110  
ENV LOG_STDOUT **Boolean**  
  
COPY vsftpd.conf /etc/vsftpd/  
COPY vsftpd_virtual /etc/pam.d/  
COPY run-vsftpd.sh /usr/sbin/  
  
RUN chmod +x /usr/sbin/run-vsftpd.sh  
RUN mkdir -p /home/vsftpd/  
RUN chown -R ftp:ftp /home/vsftpd/  
  
VOLUME /home/vsftpd  
VOLUME /var/log/vsftpd  
  
CMD ["/usr/sbin/run-vsftpd.sh"]  

