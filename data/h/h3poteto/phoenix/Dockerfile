FROM elixir:1.5.1-slim  
  
ENV APP_DIR /var/opt/app  
  
RUN set -x && \  
apt-get update && \  
apt-get install -y --no-install-recommends \  
build-essential \  
erlang-dev \  
nodejs \  
npm \  
mysql-client \  
inotify-tools \  
git \  
imagemagick \  
curl && \  
rm -rf /var/lib/apt/lists/* && \  
npm cache clean && \  
npm install n -g && \  
n stable && \  
ln -sf /usr/local/bin/node /usr/bin/node && \  
apt-get purge -y nodejs npm  
  
RUN useradd -m -s /bin/bash elixir  
RUN echo 'elixir:password' | chpasswd  
RUN mkdir -p ${APP_DIR} && \  
chown -R elixir:elixir ${APP_DIR}  
  
USER elixir  
  
WORKDIR ${APP_DIR}  
  
RUN set -x && \  
yes | mix local.hex && \  
yes | mix archive.install
https://github.com/phoenixframework/archives/raw/master/phx_new.ez  
  

