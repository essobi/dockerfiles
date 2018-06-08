FROM ruby:2.3-slim-jessie  
  
RUN echo "deb http://deb.debian.org/debian jessie-backports main contrib non-
free" >> /etc/apt/sources.list \  
&& echo "deb http://deb.debian.org/debian jessie-backports-sloppy main contrib
non-free" >> /etc/apt/sources.list \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends curl \  
&& curl -sL https://deb.nodesource.com/setup_8.x | bash - \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends \  
build-essential \  
imagemagick \  
libffi-dev libffi6 \  
libxslt1-dev libxslt1.1 \  
libxml2-dev libxml2 \  
libyaml-dev libyaml-0-2 \  
libcurl4-openssl-dev \  
libcurl3 \  
libsass-dev \  
nodejs git \  
postgresql-server-dev-all \  
openjdk-7-jre \  
&& npm install -g bower \  
&& apt-get clean  
# Web Specific Setup  
RUN gem install bundle passenger:5.1.11 \  
&& passenger-config install-standalone-runtime  
  
# Specific for tests  
ENV DOCKERIZE_VERSION v0.6.0  
RUN apt-get install -y --no-install-recommends docker wget  
RUN npm -g install phantomjs-prebuilt --unsafe-perm  
RUN wget
https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-
linux-amd64-$DOCKERIZE_VERSION.tar.gz \  
&& tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz
\  
&& rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz  

