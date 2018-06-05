FROM alpine  
  
LABEL maintainer="michael@hayslip.info"  
  
RUN apk update  
RUN apk add --progress vim wget iputils net-tools apache2 php7-common
php7-apache2 php7-curl php7-gd php7-mysqlnd php7-mysqli php7-xml php7-xmlrpc
php7-pgsql php7-iconv php7-json php7-imap php7-cgi  
RUN apk add openrc --no-cache  
RUN apk --update add tar  
  
RUN wget -O wordpress.latest.tar.gz https://wordpress.org/latest.tar.gz  
RUN tar xvzf wordpress.latest.tar.gz --keep-old-files --strip-components=1 -C
/var/www/localhost/htdocs/  
RUN rm /var/www/localhost/htdocs/index.html  
  
RUN mkdir /run/apache2  
  
RUN rc-update add apache2  
  
ENTRYPOINT [ "httpd", "-D", "FOREGROUND" ]

