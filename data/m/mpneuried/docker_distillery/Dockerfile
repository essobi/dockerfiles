FROM ubuntu:16.04  
MAINTAINER mpneuried  
  
RUN apt-get -y update  
RUN apt-get install -y sudo  
RUN sudo apt-get -y install -f build-essential wget curl  
  
RUN wget -c -O- http://packages.erlang-
solutions.com/ubuntu/erlang_solutions.asc | sudo apt-key add -  
  
RUN echo "deb http://packages.erlang-solutions.com/ubuntu xenial contrib" |
sudo tee -a /etc/apt/sources.list.d/erlang_solutions.list > /dev/null  
RUN sudo apt-get update  
  
RUN apt-get -f -y install erlang  
  
RUN erl -eval 'erlang:display(erlang:system_info(otp_release)), halt().'
-noshell  
  
# INSTALL ELIXIR  
# lend by https://github.com/c0b/docker-elixir/blob/master/1.5/Dockerfile  
# elixir expects utf8.  
ENV ELIXIR_VERSION="v1.6.1" \  
LANG=C.UTF-8  
RUN set -xe \  
&& ELIXIR_DOWNLOAD_URL="https://github.com/elixir-
lang/elixir/archive/${ELIXIR_VERSION}.tar.gz" \  
&&
ELIXIR_DOWNLOAD_SHA256="91109a1774e9040fb10c1692c146c3e5a102e621e9c48196bfea7b828d54544c"\  
&& curl -fSL -o elixir-src.tar.gz $ELIXIR_DOWNLOAD_URL \  
&& echo "$ELIXIR_DOWNLOAD_SHA256 elixir-src.tar.gz" | sha256sum -c - \  
&& mkdir -p /usr/local/src/elixir \  
&& tar -xzC /usr/local/src/elixir --strip-components=1 -f elixir-src.tar.gz \  
&& rm elixir-src.tar.gz \  
&& cd /usr/local/src/elixir \  
&& make install clean  
  
RUN elixir -v  
  
ENV PATH $PATH:/opt/elixir-${ELIXIR_V}/bin  
  
RUN mix local.hex --force  
RUN mix local.rebar --force

