FROM php:5.6.27-fpm-alpine  
  
RUN apk update  
RUN apk add g++ gcc make cmake git bash  
  
ENV APP_DIR /app  
  
RUN mkdir $APP_DIR  
WORKDIR $APP_DIR  
RUN git clone https://github.com/sharkrf/srf-ip-conn-srv.git  
RUN git clone https://github.com/sharkrf/srf-ip-conn  
RUN git clone https://github.com/zserge/jsmn  
  
RUN cp $APP_DIR/srf-ip-conn-srv/dashboard/config-example.inc.php $APP_DIR/srf-
ip-conn-srv/dashboard/config.inc.php  
  
WORKDIR $APP_DIR/srf-ip-conn-srv/build  
RUN SRF_IP_CONN_PATH=$APP_DIR/srf-ip-conn JSMN_PATH=$APP_DIR/jsmn ./build-
release.sh  
  
COPY docker-start.sh /usr/local/bin/  
  
EXPOSE 8000  
EXPOSE 65100/udp  
  
CMD ["docker-start.sh"]  

