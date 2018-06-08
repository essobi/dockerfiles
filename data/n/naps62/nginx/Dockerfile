FROM phusion/baseimage:0.9.15  
MAINTAINER Miguel Palhas <mpalhas@gmail.com>  
  
# steps required for phusino/baseimage setup  
# as specified here: https://github.com/phusion/baseimage-docker#using  
ENV HOME /root  
RUN /etc/my_init.d/00_regen_ssh_host_keys.sh  
CMD ["/sbin/my_init"]  
  
# nginx  
RUN add-apt-repository -y ppa:nginx/stable  
RUN apt-get update  
RUN apt-get install -y nginx  
RUN echo "\ndaemon off;" >> /etc/nginx/nginx.conf  
RUN rm -f /etc/nginx/sites-enabled/default  
RUN chown -R www-data:www-data /var/lib/nginx  
  
# adds nginx to runit, disabled by default  
RUN mkdir /etc/service/nginx  
RUN mkdir /etc/service/nginx-log-forwarder  
ADD runit/nginx /etc/service/nginx/run  
ADD runit/nginx-log-forwarder /etc/service/nginx-log-forwarder/run  
RUN touch /etc/service/nginx/down  
RUN touch /etc/service/nginx-log-forwarder/down  
  
# final cleanup after package installation  
# as specified here: https://github.com/phusion/baseimage-docker#using  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# configure nginx  
VOLUME ["/etc/nginx/sites-enabled", "/etc/nginx/certs", "/etc/nginx/conf.d",
"/var/log/nginx"]  
  
EXPOSE 80 443  
CMD ["nginx"]  

