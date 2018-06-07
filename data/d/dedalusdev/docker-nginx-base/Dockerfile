FROM phusion/baseimage:latest  
  
ENV HOME /root  
  
RUN /etc/my_init.d/00_regen_ssh_host_keys.sh  
  
CMD ["/sbin/my_init"]  
  
# Nginx-PHP Installation  
RUN apt-get update  
RUN apt-get install -y vim curl wget build-essential python-software-
properties  
RUN add-apt-repository -y ppa:nginx/stable  
RUN apt-get update  
  
RUN apt-get install -y nginx  
  
RUN echo "daemon off;" >> /etc/nginx/nginx.conf  
  
VOLUME ["/etc/nginx/sites-enabled", "/etc/nginx/certs", "/etc/nginx/conf.d",
"/var/log/nginx", "/var/www/html"]  
  
RUN mkdir /etc/service/nginx  
ADD build/nginx.sh /etc/service/nginx/run  
RUN chmod +x /etc/service/nginx/run  
  
EXPOSE 80  
EXPOSE 443  
# End Nginx-PHP  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

