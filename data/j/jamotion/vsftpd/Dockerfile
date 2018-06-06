FROM ubuntu:trusty  
MAINTAINER Renzo Meister <rm@jamotion.ch>  
  
RUN apt-get update && apt-get install -y --no-install-recommends vsftpd
libpam-pwdfile  
RUN apt-get clean  
  
RUN mkdir -p /var/run/vsftpd/empty  
RUN echo "auth required pam_pwdfile.so pwdfile /etc/vsftpd/ftpd.passwd" >
/etc/pam.d/vsftpd \  
&& echo "account required pam_permit.so" >> /etc/pam.d/vsftpd  
RUN useradd --home /home/vsftpd --gid nogroup -m --shell /bin/false vsftpd  
COPY vsftpd.conf /etc/vsftpd.conf  
VOLUME ["/etc/vsftpd/", "/etc/vsftpd_user_conf/"]  
  
EXPOSE 21 3000 3001 3002 3003 3004 3005  
CMD /usr/sbin/vsftpd  

