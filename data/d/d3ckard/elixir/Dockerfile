# ----------------------------------------------------------------------------  
# "THE BEER-WARE LICENSE" (Revision 42):  
# @deckard wrote this file using @trenpixster file as base. As long as you
retain this notice you  
# can do whatever you want with this stuff. I wrote it because @trenpixter
version  
# did not work well with artifacts in priv directory.  
# ----------------------------------------------------------------------------  
FROM debian:jessie  
MAINTAINER Rafał Radziszewski @d3ckard  
  
ENV REFRESHED_AT 2016-02-01  
WORKDIR /tmp  
  
# Add erlang solutions to repo list  
RUN echo "deb http://packages.erlang-solutions.com/debian jessie contrib" >>
/etc/apt/sources.list && \  
apt-key adv --fetch-keys http://packages.erlang-
solutions.com/debian/erlang_solutions.asc  
  
# Refresh the repo list  
RUN apt-get upgrade && apt-get update  
  
# Set the locale  
RUN apt-get install -y locales \  
&& echo "en_US UTF-8" >> /etc/locale.gen \  
&& locale-gen  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
RUN apt-get install -y \  
erlang=1:18.3-1 \  
git \  
unzip \  
build-essential \  
wget && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Download and Install Specific Version of Elixir  
WORKDIR /elixir  
RUN wget -q https://github.com/elixir-
lang/elixir/releases/download/v1.3.1/Precompiled.zip && \  
unzip Precompiled.zip && \  
rm -f Precompiled.zip && \  
ln -s /elixir/bin/elixirc /usr/local/bin/elixirc && \  
ln -s /elixir/bin/elixir /usr/local/bin/elixir && \  
ln -s /elixir/bin/mix /usr/local/bin/mix && \  
ln -s /elixir/bin/iex /usr/local/bin/iex  
  
# Install local Elixir hex and rebar  
RUN /usr/local/bin/mix local.hex --force && \  
/usr/local/bin/mix local.rebar --force  
  
WORKDIR /  

