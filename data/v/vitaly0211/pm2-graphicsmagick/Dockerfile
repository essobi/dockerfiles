FROM keymetrics/pm2:8  
RUN apk add --update graphicsmagick  
  
RUN apk add --update-cache \  
\--repository http://dl-3.alpinelinux.org/alpine/edge/testing \  
python \  
vips-dev \  
fftw-dev \  
&& rm -rf /var/cache/apk/*  

