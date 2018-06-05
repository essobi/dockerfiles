FROM ubuntu:16.04  
RUN apt-get update && apt-get -y install \  
vsftpd \  
finger  
  
COPY vsftpd.conf /etc/  
Run mkdir -p /srv/ftp/files && \  
chown ftp /srv/ftp/ -R && \  
chmod a-w /srv/ftp/  
  
EXPOSE 21  
VOLUME /srv/ftp/files  
  
CMD ["bash", "-c", "chmod 777 /srv/ftp/files; service vsftpd start; tail -f
/var/log/vsftpd.log"]  

