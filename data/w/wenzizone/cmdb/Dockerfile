FROM alpine:latest  
MAINTAINER wenzizone <wenzizone@126.com>  
  
EXPOSE 8989  
# install require package  
RUN apk update \  
&& apk add py-pip nodejs git \  
&& pip install django \  
&& npm install -g bower \  
&& rm -rf /var/cache/apk/*  
  
COPY . /opt/cmdb/  
RUN rm -rf /opt/cmdb/.git  
  
RUN cd /opt/cmdb/static \  
&& bower install --allow-root -f  
  
WORKDIR /opt/cmdb  
  
ENTRYPOINT ["/bin/sh","entrypoint.sh"]

