FROM ruby:2.5-alpine3.7  
  
LABEL maintainer="https://github.com/yukimochi/mastodon-assets-precompiler"  
  
ENV RAILS_ENV=production NODE_ENV=production  
  
WORKDIR /mastodon  
  
RUN apk -U upgrade \  
&& apk add -t build-dependencies \  
build-base \  
icu-dev \  
libidn-dev \  
libressl \  
libxml2-dev \  
libxslt-dev \  
postgresql-dev \  
protobuf-dev \  
python \  
&& apk add \  
ca-certificates \  
ffmpeg \  
file \  
git \  
icu-libs \  
imagemagick \  
libidn \  
libpq \  
libxml2 \  
libxslt \  
nodejs \  
nodejs-npm \  
protobuf \  
su-exec \  
tini \  
tzdata \  
yarn \  
&& update-ca-certificates \  
&& rm -rf /tmp/* /var/cache/apk/*  
  
RUN cd ~ \  
&& apk add -U cmake \  
&& git clone https://github.com/google/brotli.git \  
&& cd brotli \  
&& mkdir out \  
&& cd out \  
&& cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=./installed .. \  
&& cmake --build . --config Release --target install \  
&& cp installed/bin/brotli /usr/local/bin/ \  
&& cd /mastodon \  
&& rm -rf ~/brotli/ \  
&& apk del cmake --purge \  
&& rm -rf /tmp/* /var/cache/apk/*  
  
RUN wget https://dl.minio.io/client/mc/release/linux-amd64/mc -O
/usr/local/bin/mc \  
&& chmod +x /usr/local/bin/mc  
  
RUN git clone -b master https://github.com/tootsuite/mastodon.git . \  
&& git checkout v2.4.0  
  
RUN bundle install --deployment --without test development \  
&& yarn --pure-lockfile \  
&& yarn cache clean

