FROM alpine:3.6  
  
RUN apk add --no-cache \  
g++ \  
gcc \  
git \  
bash \  
file \  
nasm \  
make \  
automake \  
autoconf \  
gettext \  
libjpeg \  
libpng \  
libpng-dev \  
libtool \  
libnotify \  
&& apk add --update \  
nodejs \  
nodejs-npm \  
&& rm -rf /tmp/* /var/cache/apk/*  
  
CMD ["npm"]  

