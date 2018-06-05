FROM eproxus/azukiapp-erlang  
MAINTAINER Azuki <support@azukiapp.com>  
  
ENV ELIXIR_VERSION 1.0.5-2  
# Install local Elixir hex and rebar  
RUN apt-get -qq update \  
&& apt-get install -y elixir=${ELIXIR_VERSION} \  
&& /usr/local/bin/mix local.hex --force \  
&& /usr/local/bin/mix local.rebar --force \  
&& apt-get autoremove --purge \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
CMD ["iex"]  

