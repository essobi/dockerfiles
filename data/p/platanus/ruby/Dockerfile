FROM ruby:2.4  
  
MAINTAINER Juan Ignacio Donoso "juan.ignacio@platan.us"  
# Update node source  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash - \  
&& rm -rf /var/lib/apt/lists/*  
  
# Update yarn source  
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - \  
&& echo "deb https://dl.yarnpkg.com/debian/ stable main" >>
/etc/apt/sources.list.d/yarn.list  
  
# Update and install common dependencies  
RUN apt-get update && apt-get install -y \  
autoconf \  
build-essential \  
curl \  
git-core \  
imagemagick \  
libbz2-dev \  
libcurl4-openssl-dev \  
libevent-dev \  
libffi-dev \  
libglib2.0-dev \  
libjpeg-dev \  
libmagickcore-dev \  
libmagickwand-dev \  
libmysqlclient-dev \  
libncurses-dev \  
libpq-dev \  
libreadline-dev \  
libsqlite3-dev \  
libssl-dev \  
libxml2-dev \  
libxslt-dev \  
libyaml-dev \  
netcat \  
nodejs \  
zlib1g-dev \  
yarn \  
&& rm -rf /var/lib/apt/lists/*  
  
# skip installing gem documentation  
RUN echo 'gem: --no-document' >> "$HOME/.gemrc"  
  
CMD [ "irb" ]  

