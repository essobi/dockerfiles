FROM alpine:3.7  
RUN apk add --update --no-cache jq python py-pip bash \  
&& pip install --upgrade awscli \  
&& apk -v --purge del py-pip \  
&& rm -rf /var/cache/apk/*  
COPY assets /opt/resource  

