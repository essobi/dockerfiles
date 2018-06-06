FROM ubuntu:16.04  
MAINTAINER ssst0n3  
  
# 更换源为国内源  
RUN sed -i 's/archive/cn.archive/' /etc/apt/sources.list  
RUN apt-get update  
# 安装基础软件  
RUN apt-get install -y apache2 php php-sqlite3 libapache2-mod-php  
# 配置本地环境  
COPY src/ /var/www/  
# 修改apache2根目录  
RUN sed -i 's/DocumentRoot \/var\/www\/html/DocumentRoot
\/var\/www\/biscuiti/' /etc/apache2/sites-available/000-default.conf  
# 设置默认工作目录  
WORKDIR /var/www/biscuiti  
  
#CMD ["php", "-S", "0:8080"]  
RUN chmod +x /var/www/start.sh  
CMD ["/var/www/start.sh"]  

