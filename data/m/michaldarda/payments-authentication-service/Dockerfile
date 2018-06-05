FROM centos:7  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
RUN yum -y install epel-release  
RUN yum --enablerepo=epel install -y wget git build-essential make gcc
postgresql  
  
RUN wget http://packages.erlang-solutions.com/erlang-
solutions-1.0-1.noarch.rpm  
RUN rpm -Uvh erlang-solutions-1.0-1.noarch.rpm  
RUN yum -y install erlang  
  
WORKDIR /tmp/elixir-build  
RUN git clone https://github.com/elixir-lang/elixir.git  
WORKDIR elixir  
RUN git checkout v1.0.5 && make && make install  
  
RUN mix local.hex --force  
RUN mix local.rebar --force  
  
COPY . /usr/src/app  
WORKDIR /usr/src/app  
RUN elixir --erl "-smp disable" /usr/local/bin/mix deps.get  
RUN elixir --erl "-smp disable" /usr/local/bin/mix deps.compile  
  
ENV PORT 4000  
ENV MIX_ENV prod  
  
EXPOSE 4000  
CMD elixir --erl "-smp disable" /usr/local/bin/mix phoenix.server  

