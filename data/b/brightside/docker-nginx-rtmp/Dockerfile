FROM brightside/docker-ubuntu-ffmpeg  
MAINTAINER Konstantin Wilms <kon@geopacket.com>  
  
WORKDIR /home/nginx/  
ENV NGINX_VER 1.7.1  
RUN sudo apt-get -y install libpcre3-dev libssl-dev libperl-dev  
  
RUN groupadd nginx  
RUN useradd -m -g nginx nginx  
  
RUN cd /home/nginx/ && wget -q
http://nginx.org/download/nginx-${NGINX_VER}.tar.gz  
RUN cd /home/nginx/ && tar -xzvf nginx-${NGINX_VER}.tar.gz  
  
# rtmp-module  
RUN cd /home/nginx/nginx-${NGINX_VER} && git clone
git://github.com/arut/nginx-rtmp-module.git  
  
# nginx build  
RUN cd /home/nginx/nginx-${NGINX_VER} && ./configure \  
\--prefix=/usr/local \  
\--add-module=nginx-rtmp-module --with-http_perl_module --user=root && \  
make && make install  
  
RUN mkdir /etc/nginx && mkdir /var/log/nginx && mkdir /home/nginx/html  
RUN cp /home/nginx/nginx-${NGINX_VER}/conf/* /etc/nginx/  
  
ADD nginx /etc/init.d/nginx  
ADD nginx.conf.template /etc/nginx/nginx.conf.template  
ADD appinit /usr/bin/appinit  
RUN chmod 744 /usr/bin/appinit  
  
EXPOSE 80  
EXPOSE 1935  
CMD ["appinit"]  

