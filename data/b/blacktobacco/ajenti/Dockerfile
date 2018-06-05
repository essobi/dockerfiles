FROM ubuntu:14.04  
MAINTAINER Juan Giannuzzo "juan.giannuzzo@black-tobacco.com"  
#Ajenti  
RUN apt-get update  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -yq wget  
RUN rm /etc/apt/apt.conf.d/docker-gzip-indexes  
RUN wget -O- https://raw.github.com/ajenti/ajenti/1.x/scripts/install-
ubuntu.sh | sudo sh  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -yq ajenti-v ajenti-v-nginx
ajenti-v-mysql ajenti-v-php-fpm php5-mysql ajenti-v-mail ajenti-v-nodejs
ajenti-v-python-gunicorn ajenti-v-ruby-puma ajenti-v-ruby-unicorn  
  
#phpMyAdmin  
RUN wget https://files.phpmyadmin.net/phpMyAdmin/4.4.14/phpMyAdmin-4.4.14-all-
languages.tar.gz  
RUN tar -zxvf phpMyAdmin-4.4.14-all-languages.tar.gz -C /opt/  
RUN mv /opt/phpMyAdmin-4.4.14-all-languages /opt/phpMyAdmin  
ADD vh.json /etc/ajenti/vh.json  
  
#Backups  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -yq backupninja duplicity  
ADD backup /etc/backup.d/  
RUN chmod 0600 /etc/backup.* -R  
  
#Entrypoint  
ADD entrypoint.sh /usr/sbin/entrypoint.sh  
RUN chmod +x /usr/sbin/entrypoint.sh  
  
#SFTP  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -yq openssh-server  
  
RUN grep -v "Subsystem sftp /usr/lib/openssh/sftp-server" /etc/ssh/sshd_config
> /etc/ssh/sshd_config2 && mv /etc/ssh/sshd_config2 /etc/ssh/sshd_config  
RUN echo "Subsystem sftp internal-sftp" >> /etc/ssh/sshd_config  
RUN echo "Match group www-data" >> /etc/ssh/sshd_config  
RUN echo "ChrootDirectory /var/www/" >> /etc/ssh/sshd_config  
RUN echo "X11Forwarding no" >> /etc/ssh/sshd_config  
RUN echo "AllowTcpForwarding no" >> /etc/ssh/sshd_config  
RUN echo "ForceCommand internal-sftp" >> /etc/ssh/sshd_config  
  
RUN useradd -m -g www-data sftpuser  
  
#RUN chown root:www-data /srv/  
#RUN chmod 775 /srv/  
EXPOSE 80 8000 443 3306 22  
CMD ["/usr/sbin/entrypoint.sh"]  

