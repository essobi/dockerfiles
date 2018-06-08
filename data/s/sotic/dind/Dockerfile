FROM docker:stable-dind  
  
RUN apk update && \  
apk add git \  
php5 \  
openssl-dev \  
bash \  
python \  
py-pip  
  
RUN apk add --update \  
\--repository http://dl-cdn.alpinelinux.org/alpine/edge/main \  
\--repository http://dl-cdn.alpinelinux.org/alpine/edge/community \  
php7-mcrypt \  
php7-mbstring \  
php7  
  
  
RUN rm -rf /var/cache/apk/*  
  
RUN pip install awscli  

