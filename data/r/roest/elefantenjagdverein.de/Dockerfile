FROM alpine:3.6  
# greet me :)  
MAINTAINER Tobias Rös - <public@protoyou.de>  
  
# install dependencies  
RUN apk update && apk add \  
bash \  
nodejs \  
nodejs-npm \  
nginx \  
redis  
  
# remove default content  
RUN rm -R /var/www/*  
  
# create directory structure  
RUN mkdir -p /etc/nginx  
RUN mkdir -p /run/nginx  
RUN mkdir -p /etc/nginx/global  
RUN mkdir -p /var/www/html  
  
# touch required files  
RUN touch /var/log/nginx/access.log && touch /var/log/nginx/error.log  
  
# install configs  
ADD ./config/vhost.conf /etc/nginx/conf.d/default.conf  
ADD ./config/redis.conf /usr/local/etc/redis.conf  
  
# install webroot files  
ADD ./ /var/www/html/  
  
# install bower dependencies  
RUN npm install -g yarn handlebars && cd /var/www/html/ && yarn install  
  
# precompile elephant templates  
RUN cd /var/www/html/ \  
&& handlebars -c handlebars server/elephants/*/*.hbs -f
server/elephants/elephants.tpl.js \  
&& handlebars server/elephants/*/*.hbs -f
server/elephants/elephants.client.tpl.js  
  
EXPOSE 80  
EXPOSE 443  
EXPOSE 3000  
RUN chmod +x /var/www/html/config/run.sh  
ENTRYPOINT ["/var/www/html/config/run.sh"]

