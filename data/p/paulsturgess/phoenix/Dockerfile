FROM ubuntu:16.04  
MAINTAINER Paul Sturgess  
ENV REFRESHED_AT 2016-09-23  
ENV LANG=en_GB.UTF-8  
ENV LC_ALL=en_GB.UTF-8  
RUN locale-gen en_GB.UTF-8 \  
&& dpkg-reconfigure -f noninteractive locales  
  
RUN apt-get update  
RUN apt-get install -y --no-install-recommends wget  
RUN wget http://packages.erlang-solutions.com/erlang-solutions_1.0_all.deb  
RUN dpkg -i erlang-solutions_1.0_all.deb  
  
RUN apt-get update  
RUN apt-get install -y --no-install-recommends esl-erlang  
RUN apt-get install -y --no-install-recommends elixir  
RUN apt-get install -y --no-install-recommends nodejs  
RUN apt-get install -y --no-install-recommends npm  
RUN apt-get clean && rm -rf /var/lib/apt/lists/*  
  
RUN mix local.hex --force  
RUN mix local.rebar --force  
  
ENV PHOENIX_VERSION 1.2.0  
# install the Phoenix Mix archive  
RUN mix archive.install --force
https://github.com/phoenixframework/archives/raw/master/phoenix_new-$PHOENIX_VERSION.ez  
  
RUN mkdir -p /app  
WORKDIR /app  

