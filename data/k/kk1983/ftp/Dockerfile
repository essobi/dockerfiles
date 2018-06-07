FROM centos  
ENV container=docker  
RUN yum install -y initscripts  
RUN yum -y install openssl vsftpd openssh-server && rm -rf /var/cache/yum/*  
  
RUN openssl req -x509 -nodes -days 3650\  
-newkey rsa:4096 -keyout /etc/vsftpd/vsftpd.pem -out /etc/vsftpd/vsftpd.pem\  
-batch  
  
RUN ssh-keygen -f "/etc/ssh/ssh_host_rsa_key" -N '' -t rsa &&\  
ssh-keygen -f "/etc/ssh/ssh_host_ecdsa_key" -N '' -t ecdsa &&\  
ssh-keygen -f "/etc/ssh/ssh_host_ed25519_key" -N '' -t ed25519  
  
COPY vsftp.conf /etc/vsftp/vsftp.conf  
COPY vsftp_ftps.conf /etc/vsftp/vsftp_ftps.conf  
COPY vsftp_ftps_tls.conf /etc/vsftp/vsftp_ftps_tls.conf  
COPY vsftp_ftps_implicit.conf /etc/vsftp/vsftp_ftps_implicit.conf  
COPY start.sh /  
  
RUN chmod +x /start.sh  
RUN mkdir -p /home/vsftpd/  
RUN chown -R ftp:ftp /home/vsftpd/  
RUN useradd -b /home/vsftpd -ms /bin/bash public && echo 'public:public' |
chpasswd  
RUN chmod 755 /etc/vsftpd/vsftpd.pem  
  
VOLUME /home/vsftpd  
VOLUME /var/log/vsftpd  
  
EXPOSE 20 21 22 990 21100-21110 21200-21210 21300-21310 21400-21410  
ENTRYPOINT ["/start.sh"]  

