FROM ubuntu:14.04  
MAINTAINER Aldryn <aldryn@divio.ch>  
  
RUN apt-get -y update  
RUN apt-get -y upgrade  
RUN apt-get -y install nginx apache2-utils  
ADD nginx.conf /etc/nginx/sites-available/default  
RUN echo "daemon off;" >> /etc/nginx/nginx.conf  
RUN cat /etc/nginx/nginx.conf | awk '{ gsub("user www-data;","user root;");
print $0}' >> /tmp/nginx.conf.new && mv /tmp/nginx.conf.new
/etc/nginx/nginx.conf  
ADD run.sh /run.sh  
RUN chmod +x /run.sh  
ENV PASSWORD ''  
EXPOSE 4243  
CMD ["/run.sh"]  

