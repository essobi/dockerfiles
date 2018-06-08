FROM elixir:1.4  
MAINTAINER Levi Aul <levi@leviaul.com>  
  
RUN curl https://sh.rustup.rs -sSf | sh -s -- -y  
ENV PATH=/root/.cargo/bin:$PATH  
  
RUN set -xe \  
&& curl -sL https://deb.nodesource.com/setup_6.x | bash - \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends nodejs \  
&& apt-get autoremove -y --purge \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN mix do local.hex --force, \  
local.rebar --force, \  
archive.install --force
https://github.com/phoenixframework/archives/raw/master/phoenix_new-1.2.1.ez  
  
ENV MIX_ENV=prod  

