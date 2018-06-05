FROM alpine:3.2  
  
MAINTAINER Hearst Automation Team <atat@hearst.com>  
  
RUN apk update  
RUN apk add \  
ruby \  
nodejs \  
openssl \  
ca-certificates \  
curl \  
libffi \  
gdbm \  
ncurses \  
readline \  
sqlite-dev \  
tzdata \  
openssl-dev \  
zlib-dev \  
libxml2-dev \  
libxslt-dev \  
build-base \  
libgcrypt \  
ruby-bundler \  
ruby-dev \  
ruby-libs \  
gcc \  
g++ \  
make \  
linux-headers \  
&& rm /var/cache/apk/* \  
&& gem install nokogiri -- --use-system-libraries  
  
COPY gemrc /root/.gemrc  

