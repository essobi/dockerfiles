FROM ubuntu:16.04  
  
MAINTAINER RuntimeLLC  
LABEL version="0.1"  
  
ENV TZ="Europe/Moscow"  
ENV RUBY_VERSION="2.3"  
ENV FF_VERSION="45.0"  
ENV DEPENDENCIES="curl build-essential libssl-dev libreadline-dev zlib1g-dev
libpq-dev imagemagick libmagickwand-dev"  
#Time Zone Configuration  
RUN ln -snf /usr/share/zoneinfo/${TZ} /etc/localtime \  
&& echo ${TZ} > /etc/timezone  
#Install dependencies  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends ${DEPENDENCIES} \  
&& rm -rf /var/lib/apt/lists/*  
#Install and configure git  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends git \  
&& rm -rf /var/lib/apt/lists/* \  
&& git config --global url."https://github".insteadOf git://github  
  
#Install ruby, bundler  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends ruby${RUBY_VERSION}
ruby${RUBY_VERSION}-dev \  
&& gem install bundler \  
&& rm -rf /var/lib/apt/lists/*  
  
#Install Mozilla Firefox  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends libxcomposite-dev libasound2
libgtk2.0-0 \  
&& ln -s /lib/x86_64-linux-gnu/libdbus-1.so.3 /lib/x86_64-linux-gnu/libdbus-
glib-1.so.2 \  
&& rm -rf /var/lib/apt/lists/* \  
&& curl
https://ftp.mozilla.org/pub/firefox/releases/${FF_VERSION}/linux-x86_64/en-
US/firefox-${FF_VERSION}.tar.bz2 --output /tmp/firefox.tar.bz2 \  
&& tar -jxf /tmp/firefox.tar.bz2 -C /tmp/ \  
&& rm /tmp/firefox.tar.bz2 \  
&& mv /tmp/firefox /opt/firefox \  
&& ln -s /opt/firefox/firefox /usr/bin/firefox  
  
#Install X virtual framebuffer for Selenium  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends xvfb x11-xkb-utils xfonts-100dpi
xfonts-75dpi xfonts-scalable xfonts-cyrillic\  
&& rm -rf /var/lib/apt/lists/*  

