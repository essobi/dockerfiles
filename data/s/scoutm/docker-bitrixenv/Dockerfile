FROM centos:6.7  
MAINTAINER Sergey Kovalev <kovalev_s@it-in.ru>  
LABEL Description="This image is used to run Bitrix Site Manager or Bitrix24"
Version="5.1.5"  
WORKDIR /tmp  
CMD service mysqld start && service httpd start && nginx -g "daemon off;"  
RUN curl -O http://repos.1c-bitrix.ru/yum/bitrix-env.sh && sh bitrix-env.sh &&
rm -f bitrix-env.sh && yum install -y htop  
EXPOSE 80  
EXPOSE 443  
EXPOSE 5222  
EXPOSE 5223  
EXPOSE 8890  
EXPOSE 8891  
EXPOSE 8893  
EXPOSE 8894  
VOLUME ["/var/lib/mysql/","/home/bitrix/"]  

