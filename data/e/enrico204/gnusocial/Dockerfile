FROM nginx:alpine  
MAINTAINER Enrico204 <enrico204@gmail.com>  
  
RUN apk update && apk add php5-mysqli php5-fpm git curl php5-gd php5-mcrypt
php5-xml php5-iconv php5-openssl php5-dom dcron php5-curl \  
php5-imagick openssl php5-json php5-ctype php5-posix php5-gmp php5-intl && \  
rm /usr/share/nginx/html/*  
RUN git clone https://git.gnu.io/gnu/gnu-social.git -b 1.2.x
/usr/share/nginx/html/ && rm /usr/share/nginx/html/.git* -rf  
RUN apk del git && chmod a+w /usr/share/nginx/html/ && \  
mkdir /usr/share/nginx/html/avatar && chmod a+w /usr/share/nginx/html/avatar
&& \  
mkdir /usr/share/nginx/html/file && chmod a+w /usr/share/nginx/html/file  
  
COPY gnusocial.conf /etc/nginx/conf.d/default.conf  
COPY start.sh /opt/start.sh  
  
EXPOSE 80  
CMD [ "/bin/sh", "/opt/start.sh" ]  

