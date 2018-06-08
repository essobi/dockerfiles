FROM python:3-alpine  
MAINTAINER WebitDesign GbR <development@webitdesign.de>  
  
VOLUME /certs  
VOLUME /etc/letsencrypt  
EXPOSE 80 443  
RUN apk add --no-cache --virtual .build-deps linux-headers gcc musl-dev\  
&& apk add --no-cache libffi-dev openssl-dev dialog\  
&& pip install setuptools wheel ruamel.yaml certbot --no-cache-dir\  
&& apk del .build-deps\  
&& mkdir /scripts  
  
ADD crontab /etc/crontabs  
RUN crontab /etc/crontabs/crontab  
  
COPY ./scripts/ /scripts  
RUN chmod +x /scripts/ -R  
  
ENTRYPOINT ["/scripts/entrypoint.sh"]  
CMD ["/scripts/startup.sh"]  

