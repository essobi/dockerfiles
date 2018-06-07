FROM alpine  
  
RUN apk add --update \  
ca-certificates \  
git \  
openssl \  
py-pip \  
python \  
&& pip install \  
beautifulsoup4 \  
html5lib \  
requests \  
&& git clone https://gist.github.com/006a30d2f6e07213aa51.git app \  
&& apk del \  
git \  
openssl \  
py-pip \  
&& rm -rf /var/cache/apk/*  
  
WORKDIR /data  
  
CMD ["/usr/bin/python", "/app/fa_notifier.py", "/data/config.json"]

