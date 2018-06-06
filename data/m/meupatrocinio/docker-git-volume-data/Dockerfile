FROM alpine  
MAINTAINER Rafael <rafael@meupatrocinio.com>  
  
RUN echo @testing http://nl.alpinelinux.org/alpine/edge/testing >>
/etc/apk/repositories && \  
echo /etc/apk/respositories && \  
apk update && \  
apk add --no-cache bash \  
supervisor \  
curl \  
git \  
wget \  
openssh-client  
  
RUN mkdir -p /var/log/supervisor  
RUN rm -rf /var/www/app  
ADD files /attachment  
  
RUN cp -rp /attachment/supervisord.conf /etc/supervisord.conf; \  
cp -rp /attachment/deploy.sh /usr/bin/deploy.sh; \  
cp -rp /attachment/webhook /usr/bin/webhook; \  
chmod 777 /usr/bin/*;  
  
WORKDIR /var/www/  
VOLUME /var/www/  
CMD /usr/bin/python /usr/bin/supervisord -n -c /etc/supervisord.conf  
  

