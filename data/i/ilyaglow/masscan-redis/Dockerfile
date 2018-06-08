FROM alpine  
LABEL maintainer "contact@ilyaglotov.com"  
  
COPY . /masscan  
  
RUN apk update \  
&& apk add --no-cache libcap \  
libpcap-dev \  
hiredis-dev \  
\  
&& apk add --no-cache --virtual .deps build-base \  
linux-headers \  
git \  
\  
&& cd /masscan \  
&& make \  
\  
&& apk del .deps \  
&& rm -rf /var/cache/apk/*  
  
RUN adduser -D scan \  
&& setcap cap_net_raw=eip /masscan/bin/masscan  
  
USER scan  
  
VOLUME /home/scan  
  
WORKDIR /home/scan  
  
ENTRYPOINT ["/masscan/bin/masscan"]  

