FROM pygmy/postgres-repmgr:10  
MAINTAINER Maciej Lisiewski <maciej.lisiewski@gmail.com>  
ENV AWS_CONFIG_FILE=/etc/aws.config
AWS_SHARED_CREDENTIALS_FILE=/etc/aws.credentials  
  
RUN apk add --no-cache \  
groff \  
less \  
python \  
&& apk add --no-cache --virtual .build-deps py-pip \  
&& pip install awscli \  
&& apk del .build-deps  
  
ENTRYPOINT ["/sbin/tini", "--"]  
  
CMD ["repmgrd", "-f", "/repmgr.conf"]

