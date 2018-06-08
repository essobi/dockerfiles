FROM ubuntu:14.04  
# Elixir requires UTF-8  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
# Install deps  
RUN apt-get update \  
&& apt-get install -y curl \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
# Install erlang's repo  
RUN curl -sLO http://packages.erlang-solutions.com/erlang-
solutions_1.0_all.deb \  
&& dpkg -i erlang-solutions_1.0_all.deb \  
&& rm -f erlang-solutions_1.0_all.deb  
  
# Install Elixir  
RUN apt-get update \  
&& apt-get install -y elixir \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
# Install Elixir's Hex package manager  
RUN yes | mix local.hex  

