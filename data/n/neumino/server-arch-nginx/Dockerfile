FROM base/arch:latest  
MAINTAINER: Michel Tu <orphee@gmail.com>  
  
RUN pacman -Syu --noconfirm  
RUN pacman -S nginx --noconfirm  
RUN rm /etc/nginx/nginx.conf  
COPY nginx.conf /etc/nginx/nginx.conf  
  
VOLUME ["/etc/nginx/sites-enabled", "/etc/nginx/certs", "/etc/nginx/conf.d",
"/var/log/nginx"]  
  
# Define default command.  
CMD ["nginx"]  
  
# Expose ports.  
EXPOSE 80  
EXPOSE 443  

