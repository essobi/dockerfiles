FROM ruby:2.4.2  
ENV APP_HOME=/app \  
DEBIAN_FRONTEND=noninteractive \  
DEBIAN_PRIORITY=critical \  
DEBCONF_NOWARNINGS=yes  
  
# Install build essentials  
RUN apt-get update -qq && apt-get install -y \  
ca-certificates \  
build-essential \  
wget \  
curl \  
nasm \  
# Delete apt caches  
&& rm -rf /var/lib/apt/lists/*  
  
# Node source packages  
RUN curl -sL https://deb.nodesource.com/setup_9.x | bash -  
  
# Yarn source packages  
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -  
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list  
  
# wkthmltopdf  
ENV WKHTMLTOPDF_MAJOR_VERSION=0.12  
ENV WKHTMLTOPDF_VERSION=0.12.4  
RUN wget -O wkhtmltox.tar.xz
https://downloads.wkhtmltopdf.org/"$WKHTMLTOPDF_MAJOR_VERSION"/0.12.4/wkhtmltox-"$WKHTMLTOPDF_VERSION"_linux-
generic-amd64.tar.xz \  
&& tar -xf wkhtmltox.tar.xz wkhtmltox/bin/wkhtmltopdf \  
&& mv -f wkhtmltox/bin/wkhtmltopdf /usr/local/bin/wkhtmltopdf \  
&& rm -rf wkhtmltox.tar.xz wkhtmltox/  
  
# Install dependencies  
RUN apt-get update -qq && apt-get install -y \  
imagemagick \  
ghostscript \  
nodejs \  
yarn \  
&& rm -rf /var/lib/apt/lists/*  
  
# Install Dockerize  
ENV DOCKERIZE_VERSION=v0.6.0  
RUN wget
https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-
linux-amd64-$DOCKERIZE_VERSION.tar.gz \  
&& tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz
\  
&& rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz  
  
# Update Rubygems  
RUN gem update --system  
  
# Update bundler  
RUN gem install bundler  
  
# Webpack  
RUN yarn global add webpack webpack-cli \  
&& yarn cache clean  
  
# Add useful aliases  
RUN echo "alias be='bundle exec'" >> ~/.bashrc  
RUN echo "alias ll='ls -lah --color=auto'" >> ~/.bashrc  

