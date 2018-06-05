FROM nginx:latest  
  
MAINTAINER Hleb Rubanau <g.rubanau@gmail.com>  
  
RUN apt-get update && apt-get install -y certbot gettext-base  
  
# see https://github.com/moby/moby/issues/19611  
CMD ["nginx", "-g", "daemon off;"]  
EXPOSE 80 443  
VOLUME /etc/letsencrypt /var/lib/letsencrypt /etc/nginx/ssl  
ENV CERT_MODE=staging AUTOFILL_DOMAINS=false  
  
RUN sed -i -e '/conf.d/i ssl_dhparam /etc/nginx/ssl/dhparam.pem ; '
/etc/nginx/nginx.conf  
  
ADD utils /opt/nginx-le  
RUN chmod u+x /opt/nginx-le/*.sh && ln -s /opt/nginx-le/reload_nginx.sh
/usr/local/bin/reload_nginx  
  
ADD nginx_params /usr/share/nginx/nginx_params  
  
ENTRYPOINT [ "/opt/nginx-le/entrypoint.sh" ]  

