#  
#  
FROM centos  
  
LABEL maintainer = "Matthew Davis <matthew@appsoa.io>"  
LABEL repository = appsoa  
LABEL image = docker-centos-base-nginx  
LABEL built_at = 0000-00-00 00:00:00  
  
COPY src/etc /etc  
  
#COPY src/www /www  
VOLUME /www  
  
RUN useradd -g wheel user && \  
yum install -y epel-release nginx && \  
yum clean all && \  
rm -rf /etc/nginx/*_params && \  
mkdir -p /etc/nginx/ssl && \  
chown -R nginx:nginx /www && \  
cp /etc/nginx/fastcgi_params.new /etc/nginx/fastcgi_params && \  
rm -rf /usr/share/nginx  
  
# openssl genrsa -out /etc/nginx/ssl/dummy.key 2048 && \  
# openssl req -new -key /etc/nginx/ssl/dummy.key -out /etc/nginx/ssl/dummy.csr
-subj "/C=GB/L=London/O=Company Ltd/CN=docker" && \  
# openssl x509 -req -days 3650 -in /etc/nginx/ssl/dummy.csr -signkey
/etc/nginx/ssl/dummy.key -out /etc/nginx/ssl/dummy.crt  
EXPOSE 80  
COPY /entrypoint.sh /  
COPY /entrypoint.d/* /entrypoint.d/  
ONBUILD COPY /entrypoint.d/* /entrypoint.d/  
  
ENTRYPOINT ["/entrypoint.sh"]  

