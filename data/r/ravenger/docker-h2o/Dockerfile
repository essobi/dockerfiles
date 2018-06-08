FROM alpine:3.5  
MAINTAINER David Webb <ravenger@dpwlabs.com>  
  
ENV URL https://github.com/h2o/h2o.git  
ENV H2O_VERSION v2.1.0  
RUN echo "http://dl-cdn.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories \  
&& addgroup -g 1000 -S www-data \  
&& adduser -u 1000 -D -S -G www-data www-data \  
&& apk update \  
&& apk upgrade \  
# need for ocsp stapling \  
&& apk add -U perl openssl openssl-dev \  
# just needed since v2  
&& apk add -U libstdc++ \  
# save state before installed packages for building \  
&& grep ^P /lib/apk/db/installed | sed -e 's#^P:##g' | sort > /before \  
&& apk add -U build-base \  
ca-certificates \  
cmake \  
git \  
linux-headers \  
zlib-dev \  
ruby \  
ruby-dev \  
bison \  
wslay-dev \  
wslay \  
libuv-dev \  
&& git clone $URL h2o \  
# build h2o \  
&& cd h2o \  
&& git checkout $H2O_VERSION \  
&& cmake -DWITH_BUNDLED_SSL=on -DWITH_MRUBY=on . \  
&& make install \  
&& cd .. \  
&& rm -rf h2o \  
# remove packages installed just for building \  
&& grep ^P /lib/apk/db/installed | sed -e 's#^P:##g' | sort > /after \  
&& diff /before /after | grep -e "^+[^+]" | sed -e 's#+##g' | xargs -n1 apk
del \  
&& rm /before /after \  
&& rm -rf /var/cache/apk/* \  
&& mkdir /etc/h2o \  
# just test it \  
&& h2o -v  
  
ADD examples/h2o/h2o.conf /etc/h2o/  
ADD examples/www /var/www/  
WORKDIR /etc/h2o  
  
EXPOSE 80 443  
CMD ["h2o", "-m", "master", "-c", "h2o.conf"]  

