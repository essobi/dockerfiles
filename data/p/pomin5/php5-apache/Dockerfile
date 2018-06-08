FROM phusion/baseimage:0.9.15  
MAINTAINER Pomin Wu <pomin5@gmail.com>  
ENV REFRESHED_AT 2015-01-08  
ENV HOME /root  
RUN /etc/my_init.d/00_regen_ssh_host_keys.sh  
CMD ["/sbin/my_init"]  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update && \  
apt-get install -yq pwgen && \  
apt-get install -yq vsftpd && \  
apt-get install -yq php5 php-pear php5-gd php5-curl php5-sqlite php5-mysql
php5-pgsql && \  
apt-get install -yq apache2 libapache2-mod-php5 && \  
apt-get clean && rm -rf /var/lib/apt/lists/*  
  
RUN mkdir /etc/service/root  
ADD service/root.sh /etc/service/root/run  
  
RUN useradd -u 1000 -g www-data --home-dir /home/app -s /bin/bash -m app  
RUN mkdir /etc/service/app  
ADD service/app.sh /etc/service/app/run  
  
#ADD mykey.pub /tmp/mykey.pub  
#RUN cat /tmp/mykey.pub >> /root/.ssh/authorized_keys && \  
# mkdir /home/app/.ssh && \  
# chown -R app:www-data /home/app/.ssh && \  
# cat /tmp/mykey.pub >> /home/app/.ssh/authorized_keys && \  
# rm -f /tmp/mykey.pub  
RUN rm -rf /etc/apache2/sites-enabled  
ADD etc/apache2/sites-enabled /etc/apache2/sites-enabled/  
RUN mkdir -p /etc/service/apache2  
ADD service/apache2.sh /etc/service/apache2/run  
  
RUN sed -i 's/memory_limit = 128M/memory_limit = 256M/'
/etc/php5/apache2/php.ini  
  
RUN echo "local_enable=YES" >> /etc/vsftpd.conf  
RUN echo "write_enable=YES" >> /etc/vsftpd.conf  
RUN echo "local_umask=022" >> /etc/vsftpd.conf  
RUN echo "chroot_local_user=NO" >> /etc/vsftpd.conf  
RUN echo "xferlog_file=/var/log/vsftpd/vsftpd.log" >> /etc/vsftpd.conf  
RUN echo "anonymous_enable=NO" >> /etc/vsftpd.conf  
RUN mkdir -p /var/log/vsftpd  
RUN mkdir -p /var/run/vsftpd/empty  
RUN mkdir /etc/service/vsftpd  
ADD service/vsftpd.sh /etc/service/vsftpd/run  

