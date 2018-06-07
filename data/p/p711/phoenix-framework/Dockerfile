FROM elixir:1.3  
MAINTAINER Ron Arts <ron.arts@novantum.com>  
  
RUN apt-get update -q && \  
apt-get -y install \  
apt-transport-https \  
curl \  
libpq-dev \  
postgresql-client \  
inotify-tools \  
libssl1.0.0 \  
locales \  
&& apt-get clean -y && \  
rm -rf /var/cache/apt/*  
  
# elixir requires locale UTF-8  
RUN sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \  
echo 'LANG="en_US.UTF-8"'>/etc/default/locale && \  
dpkg-reconfigure --frontend=noninteractive locales && \  
update-locale LANG=en_US.UTF-8  
  
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
https://github.com/phoenixframework/archives/raw/master/phoenix_new.ez --force  
  

