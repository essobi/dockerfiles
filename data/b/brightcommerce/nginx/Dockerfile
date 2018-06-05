FROM brightcommerce/ubuntu:14.04.20140911  
MAINTAINER Brightcommerce <support@brightcommerce.com>  
  
# base  
ENV LANG en_US.UTF-8  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN locale-gen en_US en_US.UTF-8  
RUN dpkg-reconfigure locales  
RUN apt-get update  
  
RUN apt-get install -y python-software-properties  
  
# supervisor  
RUN apt-get install supervisor -y  
RUN update-rc.d -f supervisor disable  
  
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
# start script  
ADD startup /usr/local/bin/startup  
RUN chmod +x /usr/local/bin/startup  
  
CMD ["/usr/local/bin/startup"]  
  
# ppas  
RUN add-apt-repository ppa:nginx/stable -y  
RUN apt-get update  
  
# nginx  
RUN apt-get install nginx nginx-extras -y  
RUN update-rc.d -f nginx disable  
  
ADD nginx.conf /etc/nginx/nginx.conf  
  
# set volumes  
VOLUME ["/etc/nginx/sites-available", "/usr/share/nginx/html",
"/var/log/nginx", "/etc/nginx/conf.d"]  
  
# set ports  
EXPOSE 80  
# clean up  
RUN rm -rf /var/lib/apt/lists/*  

