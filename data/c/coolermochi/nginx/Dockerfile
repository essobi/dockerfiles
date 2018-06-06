FROM centos:6  
MAINTAINER coolermochi@gmail.com  
  
# nginxリポジトリ  
RUN rpm -ivh http://nginx.org/packages/centos/6/noarch/RPMS/nginx-release-
centos-6-0.el6.ngx.noarch.rpm  
  
# インストール  
RUN yum install -y nginx sudo | true  
RUN yum clean all  
  
# コンフィグ適用  
# lang  
COPY conf/i18n /etc/sysconfig/  
RUN source /etc/sysconfig/i18n && localedef -f UTF-8 -i ja_JP ja_JP.UTF-8  
  
# clock  
COPY conf/clock /etc/sysconfig/  
RUN source /etc/sysconfig/clock  
RUN \cp -p -f /usr/share/zoneinfo/Asia/Tokyo /etc/localtime  
  
# nginx  
COPY conf/nginx/nginx.conf /etc/nginx/  
COPY conf/nginx/server.conf /etc/nginx/conf.d/  
  
# services  
COPY conf/services.sh /etc/  
  
RUN chmod 777 -R /opt/ && \  
chmod 777 /etc/services.sh  
  
# html  
COPY conf/nginx/index.html /opt/  
COPY conf/nginx/40x.html /opt/  
COPY conf/nginx/50x.html /opt/  
  
# ポート開放  
EXPOSE 80  
# 起動時  
ENTRYPOINT /etc/services.sh  

