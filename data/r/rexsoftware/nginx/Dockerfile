FROM alpine:3.6  
MAINTAINER Rhys Emmerson <rhys.emmerson@siteloft.com>  
  
COPY site.conf.tmpl /start/site.conf.tmpl  
COPY start.sh /start/start.sh  
  
RUN apk add --no-cache \  
ca-certificates \  
nginx \  
dumb-init \  
libintl \  
&& apk add --no-cache --virtual build_deps \  
gettext \  
&& cp /usr/bin/envsubst /usr/local/bin/envsubst \  
&& apk del build_deps \  
&& chmod +x /start/start.sh \  
&& mkdir /www  
  
RUN mkdir /run/nginx  
  
ENTRYPOINT [ "/usr/bin/dumb-init", "--rewrite", "15:3", "--" ]  
  
CMD [ "/start/start.sh" ]

