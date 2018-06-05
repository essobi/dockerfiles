FROM ubuntu:16.04  
MAINTAINER Jak Spalding <jak@jak.io>  
  
# elixir requires the locale to be UTF8  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
ENV MIX_ENV prod  
  
# Install essentials  
RUN apt update && apt install -y curl wget zip git  
  
# Add node v6 repo  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -  
  
# Add erlang repo, and install runtime deps  
RUN wget https://packages.erlang-solutions.com/erlang-solutions_1.0_all.deb \  
&& dpkg -i erlang-solutions_1.0_all.deb \  
&& apt update \  
&& apt install -y esl-erlang elixir nodejs  
  
# Download and extract latest constable master  
RUN wget https://github.com/thoughtbot/constable/archive/master.zip \  
&& unzip master.zip && mv -T constable-master /app  
  
WORKDIR /app  
  
# Set up the phoenix project  
RUN mix local.hex --force  
RUN mix local.rebar --force  
RUN mix deps.get --only-prod  
RUN mix deps.compile  
RUN mix compile  
  
RUN npm install  
  
# Run in production  
# http://www.phoenixframework.org/v0.7.2/docs/running-in-production-or-
performance-testing  
RUN mix compile.protocols  
CMD ["elixir","-pa","_build/prod/consolidated","-S","mix","phoenix.server"]  

