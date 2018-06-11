#http://qiita.com/hnakamur/items/0b72590136cece29faee  
FROM typista/nginx-lua  
#FROM typista/nginx-lua:0.7  
# install php  
RUN wget https://raw.githubusercontent.com/typista/docker-nginx-php-
mysql/master/files/entrypoint.sh -O /etc/entrypoint.sh && \  
chmod +x /etc/entrypoint.sh && \  
rpm -Uvh http://ftp.iij.ad.jp/pub/linux/fedora/epel/6/x86_64/epel-
release-6-8.noarch.rpm && \  
rpm -Uvh http://rpms.famillecollet.com/enterprise/remi-release-6.rpm && \  
yum update -y && \  
yum install -y \--enablerepo=remi,remi-php56,epel php php-cgi php-common && \  
yum install -y \--enablerepo=remi,remi-php56,epel php-gd php-fpm php-opcache
php-devel php-mbstring php-mcrypt php-mysqlnd && \  
chmod +x /etc/entrypoint.sh  
#EXPOSE 80  
#ENTRYPOINT /etc/services.sh  

