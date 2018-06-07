FROM elixir:1.6.0  
# update and install software  
RUN apt-get install -y curl wget git openssh-client  
  
ENV PHOENIX_VERSION 1.3.0  
# install the Phoenix Mix archive  
RUN mix archive.install --force
https://github.com/phoenixframework/archives/raw/master/phx_new-$PHOENIX_VERSION.ez  
RUN mix local.hex --force \  
&& mix local.rebar --force  
  
# node.js  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash - && apt-get install
-y nodejs \  
&& rm -rf /var/cache/apt \  
&& npm install -g yarn  
  
WORKDIR /code  

