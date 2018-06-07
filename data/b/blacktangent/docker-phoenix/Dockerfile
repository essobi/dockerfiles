FROM ubuntu:latest  
  
MAINTAINER Ole J. Rosendahl <olej@blacktangent.io>  
  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
  
RUN apt-get update \  
&& apt-get upgrade -y \  
&& apt-get install -y \--no-install-recommends \  
curl \  
sudo \  
git \  
make \  
build-essential \  
ca-certificates \  
bzip2 \  
libfontconfig \  
apt-transport-https \  
&& curl -sLO http://packages.erlang-solutions.com/erlang-solutions_1.0_all.deb
\  
&& dpkg -i erlang-solutions_1.0_all.deb \  
&& apt-get update \  
&& rm erlang-solutions_1.0_all.deb \  
&& touch /etc/init.d/couchdb \  
&& apt-get install -y \--no-install-recommends \  
elixir \  
erlang-dev \  
erlang-dialyzer \  
erlang-parsetools \  
&& curl -sL https://deb.nodesource.com/setup_7.x | sudo -E bash - \  
&& apt-get install -y \--no-install-recommends \  
nodejs \  
&& curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add \- \  
&& echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee
/etc/apt/sources.list.d/yarn.list \  
&& apt-get update && apt-get install -y \--no-install-recommends \  
yarn \  
&& mkdir /tmp/phantomjs \  
&& curl -L
https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2
\  
| tar -xj --strip-components=1 -C /tmp/phantomjs \  
&& mv /tmp/phantomjs/bin/phantomjs /usr/local/bin \  
&& rm -rf /tmp/* /var/lib/apt/lists/* \  
&& apt-get clean  
  
ENV PHOENIX_VERSION 1.2.1  
  
RUN mix archive.install --force \  
https://github.com/phoenixframework/archives/raw/master/phoenix_new-$PHOENIX_VERSION.ez  
  
WORKDIR /code  

