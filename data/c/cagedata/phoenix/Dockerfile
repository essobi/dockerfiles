FROM elixir:1.3  
MAINTAINER Dave Long <dlong@cagedata.com>  
  
ENV PHOENIX_VERSION 1.2.0  
RUN apt-get -qq update \  
&& apt-get install -yqq nodejs npm \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN yes | mix local.hex  
  
RUN yes | mix archive.install
https://github.com/phoenixframework/archives/raw/master/phoenix_new-$PHOENIX_VERSION.ez  
  
EXPOSE 4000  
WORKDIR /app  
VOLUME /app  

