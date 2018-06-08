FROM ubuntu:latest  
  
# ENV Stuff  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
ENV DEBIAN_FRONTEND noninteractive  
  
# OS Update and tools  
RUN apt-get update && apt-get upgrade -y && apt-get install -y curl wget git
make xz-utils libgmp-dev libgmp10 postgresql-client inotify-tools  
  
# Erlang  
RUN wget http://packages.erlang-solutions.com/erlang-solutions_1.0_all.deb \  
&& dpkg -i erlang-solutions_1.0_all.deb \  
&& apt-get update  
RUN apt-get install -y erlang erlang-ssl erlang-inets && rm erlang-
solutions_1.0_all.deb  
  
# Elixir  
ENV ELIXIR_VERSION 1.2.0  
RUN git clone https://github.com/elixir-lang/elixir.git && cd elixir && git
checkout v$ELIXIR_VERSION && make  
ENV PATH $PATH:/elixir/bin  
  
# Hex  
RUN yes | mix local.hex  
  
# Rebar  
RUN yes | mix local.rebar  
  
# RUN mix local.hex --force  
# RUN mix local.rebar --force  
# Phoenix  
RUN yes | mix archive.install
https://github.com/phoenixframework/archives/raw/master/phoenix_new.ez  
  
# Node  
# Cant use Node 5 with latest npm because of this:
https://github.com/npm/npm/issues/9863  
# RUN curl -sLO "https://nodejs.org/dist/v4.3.1/node-v4.3.1-linux-x64.tar.xz"
&& tar -xf "node-v4.3.1-linux-x64.tar.xz" -C /usr/local --strip-components=1
&& rm "node-v4.3.1-linux-x64.tar.xz"  
RUN curl -sLO "https://nodejs.org/dist/v5.7.0/node-v5.7.0-linux-x64.tar.xz" &&
tar -xf "node-v5.7.0-linux-x64.tar.xz" -C /usr/local \--strip-components=1 &&
rm "node-v5.7.0-linux-x64.tar.xz"  
# RUN curl -sL https://deb.nodesource.com/setup_5.x | sudo -E bash -  
# RUN apt-get install -y nodejs  
# RUN npm install -g npm  
RUN npm install -g elm  
  
CMD ["/bin/bash"]  

