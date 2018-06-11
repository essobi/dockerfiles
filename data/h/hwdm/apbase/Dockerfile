FROM alpine:3.6  
MAINTAINER Howard Mei <howardleomei@gmail.com>  
ENV LOCALE en_US.UTF-8  
ENV TIMEZONE Asia/Singapore  
  
# Set Default User and Home Dir  
USER root  
ENV HOME /root  
  
# Add apk repository mirror list and user local bin  
COPY entrypoint /entrypoint  
COPY etc /etc  
COPY usr /usr  
COPY root /root  
  
ENV LANG $LOCALE  
ENV LANGUAGE $LOCALE  
ENV LC_ALL $LOCALE  
  
RUN chmod 0755 /entrypoint && chmod 0644 /etc/apk/repositories && \  
chmod 0755 /usr/local/bin/* /usr/local/sbin/* && sync && \  
apk add --update --no-cache apk-tools && apk upgrade --available && \  
apk add --update --no-cache musl musl-dev musl-utils && \  
apk add --update --no-cache grep sed tar unzip libcap su-exec && \  
set-timezone ${TIMEZONE} && apk-cleanup && ln -s /sbin/su-exec /usr/sbin/sux
&& \  
mkdir /run/cache /run/lock /run/tmp && chmod -R 0755 /run/cache /run/lock && \  
chmod -R 1777 /run/tmp && mkdir -p /var/www && chmod -R 0750 /var/www && \  
addgroup -g 82 -S www-data && adduser -u 82 -S -s /bin/sh -g 'WWW Group' \  
-G www-data -D www-data && chown -R www-data:www-data /var/www  
  
# Set Default Working Dir  
WORKDIR /var/www  
  
# Define the Entry Point and/or Default Command  
#ENTRYPOINT ["/usr/sbin/dinit", "--"]  
# You can always use following entrypoint instead, because it's included.  
ENTRYPOINT ["/entrypoint"]  
## Notice: Use ["/entrypoint"] as ENTRYPOINT instead of ["/bin/sh","-ilc"] to
avoid arg parsing issue  
## /bin/sh -ilc "arg1 arg2 ... argn" has its own builtin args parser which
demands full quoted args  
## where CMD ["cat","/etc/apk/repositories"] will cause errors and "cat
/etc/apk/repositories" will work  
## but it's incompatible with the default docker run convention. The
/entrypoint works on both styles.  

