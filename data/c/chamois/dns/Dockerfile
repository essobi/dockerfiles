FROM vladwing/tinydns  
MAINTAINER Vlad Wing <vlad.wing@gmail.com>  
COPY data tools/tinydns-data-parse.py /tmp/  
RUN apk add \--no-cache --virtual .build-deps \  
python \  
&& /tmp/tinydns-data-parse.py < /tmp/data > /etc/tinydns/data \  
&& apk del .build-deps && cd /etc/tinydns && tinydns-data # && rm -rf data
/tmp/data  

