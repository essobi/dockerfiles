# Based on marcelocg/phoenix  
FROM ubuntu:latest  
  
MAINTAINER Martin Vrkljan <mvrkljan@gmail.com>  
  
# Dependency packages and locales  
RUN apt-get -y update \  
&& apt-get upgrade -y \  
&& apt-get install -y \  
curl \  
wget \  
git \  
build-essential \  
erlang-xmerl \  
locales \  
&& locale-gen en_US.UTF-8  
  
# UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
# For some reason, installing Elixir tries to remove this file  
# and if it doesn't exist, Elixir won't install. So, we create it.  
# Thanks Daniel Berkompas for this tip.  
# http://blog.danielberkompas.com  
RUN touch /etc/init.d/couchdb  
  
# Erlang package  
RUN wget http://packages.erlang-solutions.com/erlang-solutions_1.0_all.deb \  
&& dpkg -i erlang-solutions_1.0_all.deb \  
&& apt-get update  
  
# Elixir package  
RUN apt-get install -y elixir erlang-dev erlang-parsetools erlang-tools \  
&& rm erlang-solutions_1.0_all.deb  
  
# Phoenix Mix archive  
RUN mix archive.install --force
https://github.com/phoenixframework/archives/raw/master/phx_new.ez  
  
# Hex and Rebar  
RUN mix local.hex --force \  
&& mix local.rebar --force  
  
WORKDIR /code  

