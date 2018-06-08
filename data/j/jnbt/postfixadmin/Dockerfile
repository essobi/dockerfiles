FROM alpine:3.4  
MAINTAINER Jonas Thiel <jonas@thiel.io>  
  
ENV POSTFIXADMIN_VERSION=3.2  
ENV RELEASE_DATE 2018-05-02  
ENV POSTFIXADMIN_DIR /www  
ENV POSTFIXADMIN_PACKAGE postfixadmin-$POSTFIXADMIN_VERSION  
ENV POSTFIXADMIN_DOWNLOAD
https://downloads.sourceforge.net/project/postfixadmin/postfixadmin/postfixadmin-$POSTFIXADMIN_VERSION/$POSTFIXADMIN_PACKAGE.tar.gz  
  
# Hint: dovecot is needed for `doveadm pw`  
RUN apk add --no-cache bash curl dovecot mysql-client php5-imap php5-mysqli
php5-phar php5-openssl\  
&& curl -L "$POSTFIXADMIN_DOWNLOAD" | tar xzf - \  
&& mv "$POSTFIXADMIN_PACKAGE" "$POSTFIXADMIN_DIR" \  
&& mkdir -p $POSTFIXADMIN_DIR/config/custom  
  
COPY php.ini /  
COPY config.local.php /www/  
  
COPY entrypoint.sh /sbin/entrypoint.sh  
RUN chmod 755 /sbin/entrypoint.sh  
  
EXPOSE 80  
VOLUME /www/templates_c /tmp  
WORKDIR $POSTFIXADMIN_DIR  
  
ENTRYPOINT ["/sbin/entrypoint.sh"]  
CMD ["app:start"]  

