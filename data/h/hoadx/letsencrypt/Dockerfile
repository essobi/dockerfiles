FROM alpine  
MAINTAINER Hoa Duong <duongxuanhoa@gmail.com>  
  
RUN apk --update --no-cache add certbot py-pip \  
&& pip install letsencrypt \  
&& rm -rf /var/cache/apk/* /tmp/*  
  
RUN echo "* 7,19 * * * certbot -q --no-self-upgrade renew" >>
/etc/crontabs/root  
  
VOLUME /etc/letsencrypt  
  
EXPOSE 80 443  
CMD ["crond", "-f", "-d", "8"]  

