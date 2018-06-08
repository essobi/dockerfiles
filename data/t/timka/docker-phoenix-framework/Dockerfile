FROM elixir:1.4.0  
MAINTAINER Shane Sveller <shane@shanesveller.com>  
  
RUN apt-get update -q && \  
apt-get -y install \  
apt-transport-https \  
curl \  
libpq-dev \  
postgresql-client \  
&& apt-get clean -y && \  
rm -rf /var/cache/apt/*  
  
RUN curl -s https://deb.nodesource.com/gpgkey/nodesource.gpg.key | apt-key add
- && \  
echo 'deb https://deb.nodesource.com/node_7.x jessie main' >
/etc/apt/sources.list.d/nodesource.list && \  
curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - && \  
echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list && \  
apt-get update -q && \  
apt-get install -y \  
nodejs \  
&& apt-get install yarn \  
&& apt-get clean -y && \  
rm -rf /var/cache/apt/*  
  
RUN npm install -g phantomjs-prebuilt  
RUN mix local.hex --force && \  
mix local.rebar --force  
  
ONBUILD WORKDIR /usr/src/app  
ONBUILD ENV MIX_ENV prod  
  
ONBUILD COPY . /usr/src/app/  
  
ONBUILD RUN mix do deps.get --only prod  
ONBUILD RUN yarn install  
ONBUILD RUN mix deps.compile --only prod  
  
ONBUILD RUN mix compile  

