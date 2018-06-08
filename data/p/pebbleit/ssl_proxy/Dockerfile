FROM phusion/passenger-customizable:0.9.14  
MAINTAINER Graham Gilbert <graham@pebbleit.com>  
  
RUN mkdir -p /etc/my_init.d  
ADD etc.d/ /etc/my_init.d/  
ADD substitute-env-vars.sh /substitute-env-vars.sh  
  
CMD ["/sbin/my_init"]  
  
RUN rm -f /etc/service/nginx/down  
RUN rm -f /etc/nginx/sites-available/default  
ADD nginx.conf /etc/nginx/nginx.conf  
  
VOLUME ["/var/log/nginx", "/etc/nginx/sites-templates", "/etc/nginx/ssl",
"/etc/nginx/htpasswd"]  
EXPOSE 80 443 8089

