FROM ubuntu:15.04  
MAINTAINER Daniel Dent (https://www.danieldent.com)  
  
ADD http://packages.erlang-solutions.com/ubuntu/erlang_solutions.asc
/tmp/erlang_solutions.asc  
  
ENV LANG=en_US.UTF-8  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get update -q \  
&& DEBIAN_FRONTEND=noninteractive apt-get dist-upgrade -y \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y locales \  
&& locale-gen "en_US.UTF-8" \  
&& echo "86232086a4dec44a5a505544d30822987a23a892db418f9e8e17dfff21eb0c23
/tmp/erlang_solutions.asc" | sha256sum -c \  
&& apt-key add /tmp/erlang_solutions.asc \  
&& rm /tmp/erlang_solutions.asc \  
&& echo "deb http://packages.erlang-solutions.com/ubuntu vivid contrib" >
/etc/apt/sources.list.d/erlang-solutions.list \  
&& DEBIAN_FRONTEND=noninteractive apt-get update -q \  
&& DEBIAN_FRONTEND=noninteractive apt-get dist-upgrade -y \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y erlang-base=1:18.2
erlang-dev=1:18.2 erlang-eunit=1:18.2 erlang-xmerl=1:18.2 erlang-
parsetools=1:18.2 elixir=1.2.0-1 \  
&& rm -rf /var/lib/apt/* /var/cache/apt/* \  
&& mix local.hex --force \  
&& mix local.rebar --force  

