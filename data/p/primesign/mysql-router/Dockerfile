FROM oraclelinux:7-slim  
  
ENV ROUTER_URL https://repo.mysql.com/yum/mysql-tools-
community/el/7/x86_64/mysql-router-2.1.4-1.el7.x86_64.rpm  
  
# Install server  
RUN rpmkeys --import http://repo.mysql.com/RPM-GPG-KEY-mysql \  
&& yum install -y $ROUTER_URL \  
&& yum install -y libpwquality \  
&& yum install -y hostname \  
&& rm -rf /var/cache/yum/*  
  
RUN useradd -r -d /var/lib/mysql -s /bin/false -U mysql  
  
COPY entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  
  
EXPOSE 6446 6447  
CMD [""]  

