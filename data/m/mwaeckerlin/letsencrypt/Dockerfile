FROM mwaeckerlin/base  
MAINTAINER mwaeckerlin  
ARG wwwuser="nginx"  
ENV HTTP_PORT 80  
ENV HTTPS_PORT 443  
ENV MAILCONTACT ""  
ENV LETSENCRYPT "on"  
ENV WWWUSER "${wwwuser}"  
ENV CONTAINERNAME "letsencrypt"  
ADD renew.letsencrypt.sh /etc/periodic/monthly/renew  
ADD letsencrypt-config.sh /letsencrypt-config.sh  
ADD letsencrypt-dns-authenticator.sh /letsencrypt-dns-authenticator.sh  
ADD letsencrypt-dns-cleanup.sh /letsencrypt-dns-cleanup.sh  
  
WORKDIR /tmp  
RUN adduser -SDHG $SHARED_GROUP_NAME $WWWUSER  
RUN apk add certbot dcron  
RUN mkdir -p /acme/.well-known  
RUN chown -R $WWWUSER /acme/.well-known  
RUN /cleanup.sh  
  
VOLUME /etc/letsencrypt  
EXPOSE ${HTTP_PORT} ${HTTPS_PORT}  
  
# pass inherited build arguments to children  
ONBUILD RUN mv /start.sh /letsencrypt.start.sh  
ONBUILD ADD start.sh /start.sh  
ONBUILD ADD health.sh /health.sh  
ONBUILD ARG lang  
ONBUILD ENV LANG=${lang:-${LANG}}  

