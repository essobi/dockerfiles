FROM nginx  
MAINTAINER Graham Gilbert <graham@grahamgilbert.com>  
  
ADD run.sh /run.sh  
RUN chmod 755 /run.sh  
CMD ["/run.sh"]  
  
RUN rm -f /etc/service/nginx/down  
RUN echo "\ndaemon off;" >> /etc/nginx/nginx.conf  
RUN rm -f /etc/nginx/sites-enabled/default  
ADD munki.conf /etc/nginx/sites-enabled/munki.conf  
VOLUME ["/var/log/nginx", "/usr/local/nginx/html"]  
EXPOSE 80  

