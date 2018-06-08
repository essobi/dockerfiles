FROM nginx:stable  
  
MAINTAINER Andrey Sizov, andrey.sizov@jetbrains.com  
  
ENV SERVER_NAME='_' \  
AUTH='test:YZOheU342o4OU' \  
ELK_HOST='elk.example.com' \  
SCHEME='https' \  
DOLLAR='$' \  
RESOLVER='8.8.8.8'  
COPY default.conf.template auth.htpasswd.template /etc/nginx/conf.d/  
  
EXPOSE 80  
CMD /bin/bash -c "envsubst < /etc/nginx/conf.d/default.conf.template >
/etc/nginx/conf.d/default.conf \  
&& envsubst < /etc/nginx/conf.d/auth.htpasswd.template >
/etc/nginx/conf.d/auth.htpasswd \  
&& nginx -g 'daemon off;'"

