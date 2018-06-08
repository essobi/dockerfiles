FROM mariadb:10.1  
MAINTAINER RightCtrl <support@rightctrl.com>  
LABEL Vendor="RightCtrl"  
LABEL License=GPLv2  
LABEL Version=10.1  
  
COPY galera-entrypoint.sh /usr/local/bin/  
RUN chmod +x /usr/local/bin/galera-entrypoint.sh  
RUN ln -s usr/local/bin/galera-entrypoint.sh / # backwards compat  
ENTRYPOINT ["galera-entrypoint.sh"]  
EXPOSE 3306 4444 4567 4568  
CMD ["mysqld"]

