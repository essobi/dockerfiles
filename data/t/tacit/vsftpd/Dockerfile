FROM centos:7  
MAINTAINER Tacit Knowledge <operator@tacitknowledge.com>  
LABEL Description="vsftpd Docker image based on Centos 7. Supports passive
mode and virtual users." \  
License="Apache License 2.0" \  
Usage="docker run -d -p [HOST PORT NUMBER]:21 -v [HOST FTP HOME]:/home/vsftpd
tacit/vsftpd" \  
Version="1.0"  
  
RUN yum -y update && \  
yum -y install vsftpd db4-utilsdb4 iproute && \  
yum clean all  
  
ENV FTP_USER **String**  
ENV FTP_PASS **Random**  
ENV PASV_ADDRESS **IPv4**  
ENV PASV_MIN_PORT 21100  
ENV PASV_MAX_PORT 21110  
ENV LOG_STDOUT **Boolean**  
ENV PASV_ADDR_RESOLVE NO  
  
COPY vsftpd.conf /etc/vsftpd/  
COPY vsftpd_virtual /etc/pam.d/  
COPY run-vsftpd.sh /usr/sbin/  
  
RUN chmod +x /usr/sbin/run-vsftpd.sh  
RUN mkdir -p /home/vsftpd/  
RUN chown -R ftp:ftp /home/vsftpd/  
  
VOLUME /home/vsftpd  
VOLUME /var/log/vsftpd  
  
EXPOSE 20 21  
CMD ["/usr/sbin/run-vsftpd.sh"]  

