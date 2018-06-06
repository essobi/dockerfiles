FROM alpine:3.5  
MAINTAINER hmxrobert  
  
RUN apk upgrade --update  
RUN apk add bash 'nodejs>=6.2.0' coreutils curl procps ca-certificates  
RUN apk add --virtual .build-deps git make gcc g++ autoconf automake wget curl
sudo tar xz libc-dev musl-dev eudev-dev libevent-dev  
  
RUN npm install rivarun -g  
  
RUN git clone git://github.com/kanreisa/Chinachu.git /chinachu  
  
WORKDIR /chinachu  
  
RUN echo 1 | /chinachu/chinachu installer  
  
CMD apk del --purge .build-deps  
CMD rm -rf /var/cache/apk/*  
  
VOLUME ["/mnt/chinachu"]  
  
RUN ln -s /mnt/chinachu/config.json /chinachu/config.json  
RUN ln -s /mnt/chinachu/rules.json /chinachu/rules.json  
  
RUN ln -s /mnt/chinachu/recorded /chinachu/recorded  
RUN ln -s /mnt/chinachu/data /chinachu/data  
  
RUN /chinachu/chinachu service operator initscript > /etc/init.d/chinachu-
operator  
RUN /chinachu/chinachu service wui initscript > /etc/init.d/chinachu-wui  
  
RUN chmod +x /etc/init.d/chinachu-*  
  
ADD init.sh /  
RUN chmod +x /init.sh  
  
EXPOSE 10772 20772  
CMD ["/init.sh"]  

