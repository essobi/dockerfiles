FROM alpine:3.3  
MAINTAINER WOW! Group Development  
  
RUN apk -Uv add python py-pip \  
&& pip install awscli \  
&& apk --purge -v del py-pip \  
&& rm -rf /var/cache/apk/*  
  
ENTRYPOINT ["/usr/bin/aws"]  

