FROM yobasystems/alpine:3.5-amd64  
LABEL maintainer "Dominic Taylor <dominic@yobasystems.co.uk>"
architecture="AMD64/x86_64"  
  
ENV INVOICENINJA_VERSION="3.5.1" \  
APP_ENV="production" \  
APP_URL="http://ninja.dev" \  
APP_KEY="randomappkey" \  
API_SECRET="apisecret" \  
APP_CIPHER="rijndael-128" \  
DB_TYPE="mysql" \  
DB_HOST="mysql" \  
DB_DATABASE="ninja" \  
DB_USER="ninja" \  
DB_PASSWORD="dbpassword" \  
MAIL_DRIVER="smtp" \  
MAIL_HOST="smtp.gmail.com" \  
MAIL_USERNAME="invoiceninja@gmail.com" \  
MAIL_PASSWORD="smtppassword" \  
MAIL_PORT="587" \  
MAIL_ENCRYPTION="tls" \  
MAIL_FROM_ADDRESS="invoiceninja@gmail.com" \  
MAIL_FROM_NAME="invoiceninja"  
  
RUN apk update && \  
apk add bash less vim nginx ca-certificates git tzdata zip \  
libmcrypt-dev zlib-dev gmp-dev \  
freetype-dev libjpeg-turbo-dev libpng-dev \  
php7-fpm php7-json php7-zlib php7-xml php7-pdo php7-phar php7-openssl \  
php7-pdo_mysql php7-mysqli php7-session \  
php7-gd php7-iconv php7-mcrypt php7-gmp php7-zip \  
php7-curl php7-opcache php7-ctype php7-apcu \  
php7-intl php7-bcmath php7-dom php7-mbstring php7-xmlreader mysql-client curl
&& apk add -u musl && \  
rm -rf /var/cache/apk/*  
  
RUN sed -i 's/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/g' /etc/php7/php.ini && \  
sed -i 's/expose_php = On/expose_php = Off/g' /etc/php7/php.ini && \  
sed -i
"s/nginx:x:100:101:nginx:\/var\/lib\/nginx:\/sbin\/nologin/nginx:x:100:101:nginx:\/usr:\/bin\/bash/g"
/etc/passwd && \  
sed -i
"s/nginx:x:100:101:nginx:\/var\/lib\/nginx:\/sbin\/nologin/nginx:x:100:101:nginx:\/usr:\/bin\/bash/g"
/etc/passwd- && \  
ln -s /usr/bin/php7 /usr/bin/php && \  
ln -s /sbin/php-fpm7 /sbin/php-fpm  
  
ADD files/nginx.conf /etc/nginx/  
ADD files/php-fpm.conf /etc/php7/  
ADD files/php.ini /etc/php7/  
ADD files/environment.env /environment.env  
ADD files/run.sh /  
RUN chmod +x /run.sh  
  
EXPOSE 80  
VOLUME ["/usr/html"]  
CMD ["/run.sh"]  

