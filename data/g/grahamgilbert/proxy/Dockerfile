FROM nginx  
MAINTAINER Graham Gilbert <graham@grahamgilbert.com>  
  
ADD run.sh /run.sh  
RUN chmod 755 /run.sh  
ADD render-templates.sh /render-templates.sh  
RUN chmod 755 /render-templates.sh  
ADD substitute-env-vars.sh /substitute-env-vars.sh  
RUN chmod 755 /substitute-env-vars.sh  
ADD nginx.conf /etc/nginx/nginx.conf  
RUN apt-get upgrade -y openssl  
CMD ["/run.sh"]  
  
RUN rm -f /etc/service/nginx/down  
  
VOLUME ["/var/log/nginx", "/etc/nginx/sites-templates"]  
EXPOSE 80 443  

