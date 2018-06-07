FROM nginx:alpine  
MAINTAINER UQAM/Infra  
  
RUN apk update  
RUN apk upgrade  
RUN apk add --no-cache bash git openssh php7 php7-mysqli php7-pdo php7-ctype
php7-json php7-fpm php7-curl php7-mbstring php7-pdo_mysql supervisor  
RUN rm -rf /kubernetes-policy-editor && git clone https://github.com/uqam-
infrastructures/Kubernetes-Policy-Editor /kubernetes-policy-editor  
RUN cp /kubernetes-policy-editor/application/config/database.dist.php
/kubernetes-policy-editor/application/config/database.php  
RUN cp /kubernetes-policy-editor/application/config/config.dist.php
/kubernetes-policy-editor/application/config/config.php  
COPY supervisord.conf /etc/supervisord.conf  
COPY default.conf /etc/nginx/conf.d/default.conf  
COPY auth.htpasswd /etc/nginx/conf.d/auth.htpasswd  
ADD entrypoint.sh /  
ENTRYPOINT ["/entrypoint.sh"]  
EXPOSE 80  

