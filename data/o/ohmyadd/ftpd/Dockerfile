FROM ubuntu:latest  
  
ENV FTP_USER admin  
ENV FTP_PASS admin  
ENV PASV_ADDRESS REQUIRED  
  
COPY dist /root/dist  
  
RUN apt-get update && \  
apt-get install -y --no-install-recommends vsftpd db-util && \  
apt-get clean && \  
mkdir /etc/vsftpd && \  
mv /root/dist/vsftpd_virtual /etc/pam.d/ && \  
mv /root/dist/run-vsftpd.sh /usr/sbin/ && \  
mv /root/dist/vsftpd.conf /etc/vsftpd/ && \  
mv /root/dist/keys /var/keys && \  
chmod +x /usr/sbin/run-vsftpd.sh && \  
mkdir -p /var/run/vsftpd/empty  
  
VOLUME /home/vsftpd  
VOLUME /var/log/vsftpd  
  
EXPOSE 20 21  
CMD ["/usr/sbin/run-vsftpd.sh"]  

