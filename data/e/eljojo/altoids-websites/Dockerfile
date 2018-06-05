FROM debian:wheezy  
  
# update everything because of shellshock  
RUN apt-get update && apt-get upgrade -y  
RUN apt-get upgrade -y --force-yes bash  
  
RUN apt-get install -y curl  
RUN echo "deb http://packages.dotdeb.org wheezy
all">/etc/apt/sources.list.d/dotdeb.list  
RUN echo "deb-src http://packages.dotdeb.org wheezy
all">>/etc/apt/sources.list.d/dotdeb.list  
RUN curl http://www.dotdeb.org/dotdeb.gpg | apt-key add -  
RUN apt-get update && apt-get install -y nginx-extras  
  
ADD nginx.conf /etc/nginx/nginx.conf  
RUN rm /etc/nginx/sites-enabled/default  
RUN rm /etc/nginx/sites-available/default  
  
ADD eljojo.net.conf /etc/nginx/sites-available/eljojo.net.conf  
RUN ln -s /etc/nginx/sites-available/eljojo.net.conf /etc/nginx/sites-
enabled/eljojo.net.conf  
  
ADD ajipirijou.com.conf /etc/nginx/sites-available/ajipirijou.com.conf  
RUN ln -s /etc/nginx/sites-available/ajipirijou.com.conf /etc/nginx/sites-
enabled/ajipirijou.com.conf  
  
VOLUME ["/var/log/nginx", "/var/www/eljojo.net", "/var/www/ajipirijou.com"]  
  
EXPOSE 80  
CMD ["/usr/sbin/nginx","-c","/etc/nginx/nginx.conf"]  

