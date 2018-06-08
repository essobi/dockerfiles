FROM pygmy/repmgr:3.6  
MAINTAINER Maciej Lisiewski <maciej.lisiewski@gmail.com>  
  
ENV AWS_CONFIG_FILE=/etc/aws.config ENV
AWS_SHARED_CREDENTIALS_FILE=/etc/aws.credentials  
  
RUN apk add --no-cache \  
groff \  
less \  
python \  
&& apk add --no-cache --virtual .build-deps py-pip \  
&& pip install awscli \  
&& apk del .build-deps  
  
ENTRYPOINT ["/sbin/tini", "--"]  
  
CMD ["/sbin/tini", "--", "repmgrd", "-f /repmgr.conf"]

