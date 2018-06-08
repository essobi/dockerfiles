FROM alpine:3.4  
MAINTAINER Versates <docker@versates.com>  
  
ENV LANG "en_US.UTF8"  
RUN addgroup -S mysql && adduser -h /var/lib/mysql -D -S -G mysql mysql \  
&& apk --update upgrade \  
&& apk add \  
pwgen \  
mariadb \  
mariadb-client \  
&& rm -rf /var/cache/apk/*  
  
VOLUME "/var/lib/mysql"  
  
EXPOSE 3306  
COPY entrypoint /usr/local/bin/  
ENTRYPOINT [ "entrypoint" ]  
CMD [ "mysqld" ]

