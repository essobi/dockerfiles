FROM alpine:3.6  
  
COPY Gemfile* /  
  
RUN mkdir -p /opt /srv \  
&& \  
apk add \--no-cache --virtual .build-deps build-base python2-dev libffi-dev
openssl-dev bash ruby-dev \  
&& \  
apk add \--no-cache ruby ruby-bundler python curl ca-certificates py2-pip \  
&& \  
gem install --no-document --clear-sources -g \  
&& \  
pip --no-cache-dir install pyopenssl \  
&& \  
curl https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-
sdk-176.0.0-linux-x86_64.tar.gz | tar -xz -C /opt \  
&& \  
rm -rf /tmp/* \  
&& \  
apk del --no-cache .build-deps  
  
ENV PATH="${PATH}:/opt/google-cloud-sdk/bin"  
WORKDIR /srv

