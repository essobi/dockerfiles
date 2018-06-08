FROM ruby:2.3-alpine  
LABEL Author="Lyndon"  
  
ENV S6_OVERLAY_VERSION 1.21.4.0  
RUN apk add --no-cache \  
build-base libgcrypt-dev gcc make git curl-dev nodejs bison gawk gpgme tar vim
bash tzdata procps linux-headers \  
ruby-dev ruby-libs openssl-dev libc-dev zlib-dev libxml2-dev libxslt-dev yaml-
dev gmp-dev \  
postgresql-dev imagemagick-dev readline-dev libffi-dev gdbm-dev && \  
cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \  
mkdir /temp  
# Add s6-overlay  
ADD https://github.com/just-
containers/s6-overlay/releases/download/v$S6_OVERLAY_VERSION/s6-overlay-
amd64.tar.gz /temp/  
  
COPY . /temp  
RUN cd /temp \  
&& bundle config build.nokogiri --use-system-libraries \  
&& bundle install \  
&& tar xzf /temp/s6-overlay-amd64.tar.gz -C / \  
&& rm -rf /var/cache/apk/* \  
&& rm -rf /temp  
  
ENTRYPOINT ["/init"]  

