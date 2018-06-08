#WOO COMMENTS  
FROM debian:testing  
MAINTAINER Pyromancer <pyromancer@fireinthedeep.com>  
RUN apt-get update && apt-get install -y build-essential pkg-config cmake git
checkinstall software-properties-common sudo wget  
RUN add-apt-repository non-free  
RUN add-apt-repository contrib  
RUN apt-get update  
RUN apt-get install -y cron logrotate make build-essential libssl-dev
zlib1g-dev libpcre3 libpcre3-dev curl  
RUN groupadd nginx  
RUN useradd -m -g nginx nginx  
RUN echo "nginx ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers  
RUN chmod 0440 /etc/sudoers  
USER nginx  
ENV HOME /home/nginx  
WORKDIR /home/nginx  
RUN git clone git://github.com/arut/nginx-rtmp-module.git  
RUN sudo mkdir /var/www && sudo cp /home/nginx/nginx-rtmp-module/stat.xsl
/var/www/stat.xsl && sudo chown -R nginx:nginx /var/www  
RUN wget http://nginx.org/download/nginx-1.2.4.tar.gz && tar xzf
nginx-1.2.4.tar.gz  
RUN cd ./nginx-1.2.4 && ./configure --with-ipv6 --add-
module=/home/nginx/nginx-rtmp-module && make  
RUN cd ./nginx-1.2.4/ && sudo make install  

