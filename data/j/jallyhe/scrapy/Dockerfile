#python3 scrapy  
FROM alpine:latest  
RUN echo "Asia/Shanghai" > /etc/timezone  
#RUN echo "https://mirror.tuna.tsinghua.edu.cn/alpine/v3.7/main" >
/etc/apk/repositories  
RUN apk add --update \  
python3 \  
python3-dev \  
gcc \  
openssl-dev \  
libxml2 \  
libxml2-dev \  
libffi \  
libffi-dev \  
libxslt-dev \  
py-pip \  
build-base \  
&& pip3 install scrapy \  
&& rm -rf /var/cache/apk/*  

