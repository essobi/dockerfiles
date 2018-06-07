FROM phusion/baseimage  
MAINTAINER Joe Dytrych <joe@drumrollhq.com>  
  
ENV HOME /root  
EXPOSE 80  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init"]  
RUN rm -rf /etc/service/sshd /etc/my_init.d/00_regen_ssh_host_keys.sh  
  
# Dependencies have dependencies.  
RUN apt-get update  
RUN apt-get install -y python-software-properties curl build-essential git
fontconfig  
  
# Node:  
RUN curl -sL https://deb.nodesource.com/setup | bash -  
RUN apt-get install -y nodejs  
  
# ffmpeg & nginx:  
RUN add-apt-repository ppa:jon-severinsson/ffmpeg  
RUN add-apt-repository ppa:nginx/stable  
RUN apt-get update  
RUN apt-get install -y ffmpeg nginx  
  
# Build tools:  
RUN npm install -g gulp bower  
  
# Web Server:  
COPY ./conf/nginx/nginx.conf /etc/nginx/nginx.conf  
RUN rm /etc/nginx/sites-enabled/default  
COPY ./conf/nginx/site.conf /etc/nginx/sites-enabled/default  
  
# Services  
RUN mkdir /etc/service/nginx  
COPY ./conf/services/nginx.sh /etc/service/nginx/run  
COPY ./conf/services/node.sh /etc/service/node/run  
  
# Copy over files, etc.  
RUN mkdir /build_tmp  
ADD ./game /build_tmp/game  
ADD ./website /build_tmp/website  
ADD ./server /build_tmp/server  
  
# Git confuses bower somehow?  
RUN rm -rf /build_tmp/**/.git  
  
# Game  
WORKDIR /build_tmp/game  
RUN npm install  
  
# Fix imagemin dep dodgyness  
WORKDIR /build_tmp/game/node_modules/gulp-imagemin/node_modules/imagemin  
RUN rm -rf node_modules  
RUN npm install  
WORKDIR /build_tmp/game  
  
RUN bower --allow-root install  
RUN gulp build -o  
RUN mv /build_tmp/game/public /srv/game  
  
# Website  
WORKDIR /build_tmp/website  
RUN npm install  
RUN bower --allow-root install  
RUN gulp optimize  
RUN mv /build_tmp/website/public /srv/website  
  
# Server  
WORKDIR /build_tmp/server  
RUN npm install  
RUN mv /build_tmp/server /srv/server  
ENV NODE_ENV production  
ENV REDIS_DB 0  
ENV PORT 3000  
ENV EAK_STATIC ../merged  
  
# Merged serve folder  
RUN mkdir /srv/merged/  
RUN cp -r /srv/game/* /srv/merged  
RUN cp -r /srv/website/* /srv/merged  
  
# Clean Up  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

