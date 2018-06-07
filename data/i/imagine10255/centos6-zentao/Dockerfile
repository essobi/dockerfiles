FROM centos:centos6  
MAINTAINER Imagine Chiu<imagine10255@gmail.com>  
  
  
ENV SSH_PASSWORD=P@ssw0rd  
  
  
# Install base tool  
RUN yum -y install vim wget tar  
  
# Install develop tool  
RUN yum -y groupinstall development  
  
# Install php rpm  
#RUN rpm --import http://ftp.riken.jp/Linux/fedora/epel/RPM-GPG-KEY-EPEL-6 &&
\  
# rpm -Uvh https://mirror.webtatic.com/yum/el6/latest.rpm  
# Install SSH Service  
RUN yum install -y openssh-server passwd  
RUN sed -ri 's/#UsePAM no/UsePAM no/g' /etc/ssh/sshd_config && \  
echo "${SSH_PASSWORD}" | passwd "root" \--stdin  
  
# Install crontab service  
RUN yum -y install vixie-cron crontabs  
  
# Install php-fpm (https://webtatic.com/packages/php56/  
#RUN yum -y install php56w php56w-fpm php56w-mbstring php56w-xml php56w-mysql
php56w-mssql php56w-pdo php56w-mcrypt php56w-gd php56w-pecl-imagick
php56w-opcache php56w-pecl-memcache php56w-pecl-xdebug  
# Install Zentao  
RUN wget http://dl.cnezsoft.com/zentao/8.1.3/ZenTaoPMS.8.1.3.zbox_64.tar.gz  
  
# Install Zentao  
RUN tar zxvf ZenTaoPMS.8.1.3.zbox_64.tar.gz -C /opt/ && \  
/opt/zbox/zbox start  
  
# Copy files for setting  
ADD . /opt/  
  
# Create Base Enter Cont Command  
#RUN chmod 755 /opt/docker/bash/init-bashrc.sh && echo "/opt/docker/bash/init-
bashrc.sh" >> /root/.bashrc && \  
# echo 'export PATH="/root/.composer/vendor/bin:$PATH"' >> /root/.bashrc  
# Setting lnmp(php,lnmp)  
#RUN chmod 755 /opt/docker/bash/setting-lnmp.sh && bash
/opt/docker/bash/setting-lnmp.sh  
# Setting DateTime Zone  
RUN cp -p /usr/share/zoneinfo/Asia/Taipei /etc/localtime  
  
# Setup default path  
WORKDIR /home  
  
# Private expose  
EXPOSE 22 80  
# Volume for web server install  
VOLUME ["/home/website","/home/config","/home/logs"]  
  
# Start run shell  
CMD ["bash"]  

