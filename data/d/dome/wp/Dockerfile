FROM wordpress:php7.2-fpm-alpine  
MAINTAINER Dome C. <dome@tel.co.th>  
  
RUN apk update \  
&& apk add --no-cache \  
bash \  
less \  
vim \  
nginx \  
ca-certificates \  
openssh-client \  
git \  
curl \  
rsync \  
musl \  
&& apk --update --no-cache add tar redis libjpeg-turbo-utils libwebp-tools
optipng gifsicle  
RUN rm -rf /var/cache/apk/*  
  
ENV TERM="screen-256color" \  
DB_HOST="172.17.0.1" \  
DB_NAME="" \  
DB_USER=""\  
DB_PASS=""  
ENV PATH /DATA/bin:$PATH  
  
#RUN sed -i 's/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/g' /etc/php7/php.ini &&
\  
# sed -i 's%\;session.save_path.*%session.save_path = /DATA/sessions%'
/etc/php7/php.ini && \  
RUN sed -i
"s/nginx:x:100:101:nginx:\/var\/lib\/nginx:\/sbin\/nologin/nginx:x:100:101:nginx:\/DATA:\/bin\/bash/g"
/etc/passwd && \  
sed -i
"s/nginx:x:100:101:nginx:\/var\/lib\/nginx:\/sbin\/nologin/nginx:x:100:101:nginx:\/DATA:\/bin\/bash/g"
/etc/passwd-  
  
RUN apk --no-cache add shadow && groupmod -g 1001 nginx && usermod -u 1001
nginx  
  
COPY .bashrc /root/  
COPY shells /etc  
ADD files/nginx.conf /etc/nginx/  
ADD files/php-fpm.conf /usr/local/etc/  
ADD files/run.sh /  
ADD files/wp-config-devoply.php /usr/bin/wp-config-devoply  
ADD files/docker-entrypoint.sh /usr/local/bin/  
RUN chmod +x /run.sh && chmod +x /usr/bin/wp-config-devoply && chmod +x
/usr/local/bin/docker-entrypoint.sh  
COPY .bashrc /root/  
COPY shells /etc  
#ENV TERM screen-256color  
ENV SHELL=/bin/bash  
  
RUN curl -O https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-
cli.phar && chmod +x wp-cli.phar && mv wp-cli.phar /usr/bin/wp && chown
nginx:nginx /usr/bin/wp  
  
EXPOSE 80  
VOLUME /DATA  
WORKDIR /DATA/html  
  
#CMD ["/run.sh"]  
ENTRYPOINT ["docker-entrypoint.sh"]  
CMD ["php-fpm"]  

