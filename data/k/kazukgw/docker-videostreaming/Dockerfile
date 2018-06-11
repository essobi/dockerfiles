FROM kazukgw/docker-ffmpeg  
WORKDIR /home/nginx/  
  
RUN sudo apt-get -y install libpcre3-dev libssl-dev  
  
RUN groupadd nginx  
RUN useradd -m -g nginx nginx  
  
RUN cd /home/nginx/ && wget -q http://nginx.org/download/nginx-1.7.1.tar.gz  
RUN cd /home/nginx/ && tar -xzvf nginx-1.7.1.tar.gz  
  
# rtmp-module  
RUN cd /home/nginx/nginx-1.7.1 && git clone git://github.com/arut/nginx-rtmp-
module.git  
  
# nginx build  
RUN cd /home/nginx/nginx-1.7.1 && ./configure \  
\--prefix=/usr/local \  
\--add-module=nginx-rtmp-module --user=nginx && \  
make && make install  
  
RUN mkdir /etc/nginx && mkdir /var/log/nginx && mkdir /home/nginx/html  
RUN cp /home/nginx/nginx-1.7.1/conf/* /etc/nginx/  
  
ADD nginx /etc/init.d/nginx  
ADD nginx.conf.template /etc/nginx/nginx.conf.template  
ADD appinit /usr/bin/appinit  
RUN chmod 744 /usr/bin/appinit  
  
EXPOSE 80  
EXPOSE 1935  
CMD ["appinit"]  

