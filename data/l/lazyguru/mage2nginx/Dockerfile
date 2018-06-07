FROM lazyguru/mage2base  
  
# Installing Nginx  
RUN wget http://nginx.org/packages/centos/6/noarch/RPMS/nginx-release-
centos-6-0.el6.ngx.noarch.rpm  
RUN rpm -ivh nginx-release-centos-6-0.el6.ngx.noarch.rpm  
RUN yum -y install nginx && yum clean all  
RUN rm -f nginx-release-centos-6-0.el6.ngx.noarch.rpm  
  
ADD etc/nginx.conf/fastcgi_params.conf /etc/nginx/conf/fastcgi_params.conf  
ADD etc/nginx.conf/magento.conf /etc/nginx/conf/magento.conf  
RUN mv /etc/nginx/conf.d/default.conf /etc/nginx/conf.d/default.conf.default  
ADD etc/nginx.conf/default.conf /etc/nginx/conf.d/default.conf  
ADD etc/nginx.conf/nginx.conf /etc/nginx/nginx.conf  
  
RUN mkdir -p /var/www/html  
RUN chown -Rf nginx:nginx /var/www/html  
  
VOLUME ["/var/www/html"]  
  
EXPOSE 443  
EXPOSE 8080  
ADD scripts/start.sh /start.sh  
RUN chmod 755 /start.sh  
  
CMD ["/bin/bash", "/start.sh"]  

