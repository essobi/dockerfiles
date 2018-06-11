FROM alpine:3.6  
MAINTAINER VanityShed  
  
ENV GIT_URL https://github.com/samr7/vanitygen  
ENV REFRESHED_AT 2017-06-28  
# install dependencies  
RUN set -x \  
&& apk add --no-cache git libqrencode openssl-dev pcre-dev gegl-dev build-base
\  
&& cd /root \  
&& git clone $GIT_URL \  
&& cd /root/vanitygen \  
&& make \  
&& apk del --purge git build-base  
  
ENTRYPOINT ["/root/vanitygen/vanitygen"]  
CMD ["--help"]  

