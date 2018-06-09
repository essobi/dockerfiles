FROM centos:latest  
  
MAINTAINER niikunihiro  
  
# Apache インストール  
RUN ["yum", "-y", "install", "httpd"]  
  
# コンテンツの配置  
ADD ["html/", "/var/www/html/"]  
  
# 公開ポートの設定  
EXPOSE 80  
CMD ["/usr/sbin/httpd","-D", "FOREGROUND"]  

