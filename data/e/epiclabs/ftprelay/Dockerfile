FROM ubuntu:14.04  
RUN apt-get update && apt-get install -y \  
curlftpfs \  
vsftpd \  
libpam-pwdfile \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN mkdir -p /ftp/ /chroot/ /etc/vsftpd/userconf.d/  
RUN useradd --home /ftp --gid nogroup -m --shell /bin/false vsftpd  
RUN chown -R vsftpd:nogroup /ftp/  
  
ADD /etc/vsftpd/ /etc/vsftpd/  
ADD /etc/pam.d/ /etc/pam.d/  
  
ADD /entrypoint.sh /  
  
CMD ["/entrypoint.sh"]  

