FROM alpine:3.3  
MAINTAINER WOW! Group Development  
  
RUN apk -Uv add python py-pip \  
&& apk -UvX http://dl-4.alpinelinux.org/alpine/edge/main add postgresql \  
&& pip install awscli \  
&& apk --purge -v del py-pip \  
&& rm -rf /var/cache/apk/*  
ADD dump /  
  
ENTRYPOINT ["/dump"]  

