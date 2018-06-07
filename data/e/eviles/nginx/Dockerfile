FROM eviles/centos-sshd  
  
RUN rpm -Uvh http://nginx.org/packages/centos/7/noarch/RPMS/nginx-release-
centos-7-0.el7.ngx.noarch.rpm \  
&& yum -y install epel-release \  
&& yum -y install certbot nginx \  
&& yum clean all \  
&& rm -rf /var/cache/yum/* \  
&& echo "[program:nginx]" >> /etc/supervisord.conf \  
&& echo "command=/run_nginx.sh" >> /etc/supervisord.conf \  
&& echo "stdout_logfile=/dev/stdout" >> /etc/supervisord.conf \  
&& echo "stdout_logfile_maxbytes=0" >> /etc/supervisord.conf \  
&& echo "stderr_logfile=/dev/stderr" >> /etc/supervisord.conf \  
&& echo "stderr_logfile_maxbytes=0" >> /etc/supervisord.conf  
  
ADD default.conf.template /etc/nginx/default.conf.template  
ADD ssl.conf.template /etc/nginx/ssl.conf.template  
ADD run_nginx.sh /run_nginx.sh  
RUN chmod 755 /run_nginx.sh  
  
EXPOSE 80 443  

