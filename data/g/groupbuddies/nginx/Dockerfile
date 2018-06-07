FROM phusion/baseimage:0.9.15  
MAINTAINER Miguel Palhas <mpalhas@gmail.com>  
  
# steps required for phusino/baseimage setup  
# as specified here: https://github.com/phusion/baseimage-docker#using  
ENV HOME /root  
RUN /etc/my_init.d/00_regen_ssh_host_keys.sh  
CMD ["/sbin/my_init"]  
  
# nginx  
RUN apt-get update \  
&& apt-get -y install nginx-extras \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN echo "\ndaemon off;" >> /etc/nginx/nginx.conf  
RUN rm -f /etc/nginx/sites-enabled/default  
  
# adds nginx to runit, disabled by default  
RUN mkdir /etc/service/nginx  
ADD runit/nginx /etc/service/nginx/run  
  
# configure nginx  
VOLUME ["/etc/nginx/sites-enabled", "/etc/nginx/certs", "/etc/nginx/conf.d",
"/var/log/nginx"]  
  
EXPOSE 80 443  

