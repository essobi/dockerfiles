FROM alpine:3.2  
RUN apk add --update php-cli php-phar php-zlib php-json php-ctype && rm -rf
/var/cache/apk/*  
  
RUN php -r "readfile('http://symfony.com/installer');" >
/usr/local/bin/symfony && chmod +x /usr/local/bin/symfony  
  
WORKDIR "/home"  
  
ENTRYPOINT ["/usr/local/bin/symfony", "--ansi"]  

