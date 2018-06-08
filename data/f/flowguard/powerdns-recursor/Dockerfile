FROM alpine:latest  
  
RUN sed -i -e 's#alpine/v[0-9.]*/#alpine/edge/#g' /etc/apk/repositories \  
&& apk --update --no-cache add \  
tini \  
py2-pip \  
pdns-recursor \  
&& pip install envtpl \  
&& rm /var/cache/apk/*  
  
COPY recursor.conf.tpl /etc/pdns/recursor.conf.tpl  
COPY start.sh /  
  
ENTRYPOINT [ "tini", "-vv", "/start.sh" ]  
CMD [ "/usr/sbin/pdns_recursor", "--disable-syslog=yes", "--daemon=no", "--
local-address=0.0.0.0" ]  

