FROM composer/satis  
  
RUN apk --no-cache add nginx-lua  
  
ADD nginx/default /etc/nginx/nginx.conf  
  
ENV COMPOSER_ALLOW_SUPERUSER 1  
ENV COMPOSER_NO_INTERACTION 1  
ENV COMPOSER_HOME /satis/web/.composer  
ENV SATIS_CONFIG_FILE /satis/satis.json  
ENV LOOPER_PERIOD 30  
ENV DELAY_BEFORE_BUILD 5  
ADD satis.json /satis/satis.json  
ADD bin/ /satis/bin/  
RUN chmod +x /satis/bin/*  
RUN mkdir /satis/web  
  
WORKDIR /satis  
  
VOLUME /satis/web  
  
CMD ["/satis/bin/run.sh"]  
  
EXPOSE 80  

