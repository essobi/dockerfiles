FROM ubuntu:16.04  
  
MAINTAINER Janis Miezitis <janjiss@gmail.com>  
  
# Elixir requires UTF-8  
ENV LANG en_US.UTF-8 \  
LANGUAGE en_US:en \  
LC_ALL en_US.UTF-8  
  
  
RUN locale-gen en_US.UTF-8 && \  
apt-get update -y && \  
apt-get install -y curl wget git make imagemagick && \  
  
# install Node.js (>= 5.0.0) and NPM in order to satisfy brunch.io
dependencies  
# See http://www.phoenixframework.org/docs/installation#section-node-js-5-0-0-  
curl -sL https://deb.nodesource.com/setup_5.x | bash && \  
apt-get install -y nodejs && \  
  
# download and install Erlang package  
wget http://packages.erlang-solutions.com/erlang-solutions_1.0_all.deb && \  
dpkg -i erlang-solutions_1.0_all.deb && \  
apt-get install -y elixir erlang-dev erlang-parsetools && \  
rm erlang-solutions_1.0_all.deb && \  
  
# Install latest hex  
mix local.hex && mix local.rebar && \  
  
# install the Phoenix Mix archive  
mix archive.install
https://github.com/phoenixframework/archives/raw/master/1.2-rc/phoenix_new.ez
&& \  
apt-get autoremove && \  
apt-get autoclean && \  
rm -rf /var/lib/apt/lists/*  
  
WORKDIR /code  

