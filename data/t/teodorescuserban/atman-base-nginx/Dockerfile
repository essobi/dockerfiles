FROM teodorescuserban/atman-base:latest  
  
MAINTAINER Serban Teodorescu, teodorescu.serban@gmail.com  
  
RUN apt-get -qq update  
  
RUN apt-get install -qq -y \  
nginx-extras  
# nginx-full  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN mkdir -p /etc/service/nginx  
ADD run /etc/service/nginx/  
RUN chmod u+x /etc/service/nginx/run  
  
RUN cp /etc/nginx/nginx.conf /etc/nginx/nginx.orig  
RUN echo "daemon off;" >> /etc/nginx/nginx.conf  
  
EXPOSE 80  
EXPOSE 443  
VOLUME ['/srv/www', '/var/log/nginx']  
  
RUN /etc/my_init.d/00_regen_ssh_host_keys.sh  
  
CMD ["/sbin/my_init"]  

