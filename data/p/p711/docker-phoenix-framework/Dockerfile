FROM elixir:1.4  
MAINTAINER Ron Arts <ron.arts@novantum.com>  
  
RUN apt-get update -q && \  
apt-get -y install \  
apt-transport-https \  
ca-certificates \  
curl \  
libpq-dev \  
postgresql-client \  
inotify-tools \  
&& apt-get clean -y && \  
rm -rf /var/cache/apt/*  
  
RUN apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys
58118E89F3A912897C070ADBF76221572C52609D && \  
echo 'deb https://apt.dockerproject.org/repo debian-jessie testing' >
/etc/apt/sources.list.d/docker.list && \  
apt-get update -q && \  
apt-get install -y docker-engine && \  
apt-get clean -y && \  
rm -rf /var/cache/apt/*  
  
RUN curl -s https://deb.nodesource.com/gpgkey/nodesource.gpg.key | apt-key add
- && \  
echo 'deb https://deb.nodesource.com/node_4.x jessie main' >
/etc/apt/sources.list.d/nodesource.list && \  
apt-get update -q && \  
apt-get install -y \  
nodejs \  
&& apt-get clean -y && \  
rm -rf /var/cache/apt/*  
  
RUN npm install -g npm@3.8.9  
RUN mix local.hex --force && \  
mix local.rebar --force && \  
mix archive.install
https://github.com/phoenixframework/archives/raw/master/phx_new.ez --force &&
\  
rebar3 local upgrade  
  
ONBUILD WORKDIR /usr/src/app  
ONBUILD ENV MIX_ENV prod  
  
ONBUILD COPY mix.* /usr/src/app/  
ONBUILD RUN mix do deps.get --only prod  
# phoenix and phoenix_html JS dependencies are included from Hex packages  
ONBUILD COPY package.json /usr/src/app/  
ONBUILD RUN npm install  
ONBUILD RUN mix deps.compile --only prod  
  
ONBUILD COPY . /usr/src/app/  
ONBUILD RUN mix compile  

