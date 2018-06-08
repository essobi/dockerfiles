FROM debian:jessie  
MAINTAINER Lyndon li <snakeliwei@gmail.com>  
  
RUN apt-get update \  
&& apt-get install -qy git \  
curl \  
imagemagick \  
libmagickcore-dev \  
libmagickwand-dev \  
libpq-dev \  
libcurl3-dev \  
nodejs \  
vim  
  
ENV RUBY_VERSION 2.1.0  
ENV S6_OVERLAY_VERSION 1.18.1.3  
# Add s6-overlay  
ADD https://github.com/just-
containers/s6-overlay/releases/download/v$S6_OVERLAY_VERSION/s6-overlay-
amd64.tar.gz /tmp/  
RUN tar xzf /tmp/s6-overlay-amd64.tar.gz -C / &&\  
rm /tmp/s6-overlay-amd64.tar.gz  
  
# Install RVM, RUBY, bundler  
RUN gpg --keyserver hkp://keys.gnupg.net --recv-keys
409B6B1796C275462A1703113804BB82D39DC0E3 \  
&& \curl -sSL https://get.rvm.io | bash -s stable \  
&& /bin/bash -l -c "rvm requirements" \  
&& /bin/bash -l -c "rvm install $RUBY_VERSION" \  
&& /bin/bash -l -c "rvm use $RUBY_VERSION --default" \  
&& /bin/bash -l -c "gem install bundler --no-ri --no-rdoc" \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
ENTRYPOINT ["/init"]  

