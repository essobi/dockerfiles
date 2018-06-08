FROM ubuntu:15.04  
  
MAINTAINER Vincent Palmer <shift@someone.section.me>  
  
RUN apt-get update \  
&& apt-get upgrade --yes \  
&& apt-get install --yes erlang-nox erlang-dev erlang-reltool libssl-dev \  
erlang-eunit git build-essential erlang-os-mon erlang-src \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

