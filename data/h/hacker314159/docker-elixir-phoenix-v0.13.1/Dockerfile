# This Dockerfile based on
https://registry.hub.docker.com/u/marcelocg/phoenix/  
# marcelocg/phoenix installs phoenix version 0.11.1  
# this installs phoenix version 0.13.1  
FROM ubuntu:15.04  
MAINTAINER Steven Li <sli@bleacherreport.com>  
  
# Elixir requires UTF-8  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
# Install curl, wget, git, and make  
RUN apt-get update && apt-get upgrade -y && apt-get install -y curl wget git
make  
  
# download and install Erlang packages  
RUN wget http://packages.erlang-solutions.com/erlang-solutions_1.0_all.deb \  
&& dpkg -i erlang-solutions_1.0_all.deb \  
&& apt-get update  
  
# Install Erlang from package  
RUN apt-get -y install erlang erlang-ssl erlang-inets && rm erlang-
solutions_1.0_all.deb  
  
# Install Elixir  
RUN apt-get -y install elixir  
  
# Install rebar (Erlang's Mix) and Hex (Elixir's Package Manager)  
RUN mix local.rebar \  
&& mix local.hex --force  
  
# Fetch phoenix installer version 0.13.1  
RUN mix archive.install
https://github.com/phoenixframework/phoenix/releases/download/v0.13.1/phoenix_new-0.13.1.ez
--force  
  
# Download and Install npm  
RUN gpg --keyserver pool.sks-keyservers.net --recv-keys
7937DFD2AB06298B2293C3187D33FF9D0246406D
114F43EE0176B71C7BC219DD50A3051F888C628D  
  
ENV NODE_VERSION 0.12.2  
ENV NPM_VERSION 2.7.3  
RUN curl -SLO "http://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-
linux-x64.tar.gz" \  
&& curl -SLO "http://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt.asc" \  
&& gpg --verify SHASUMS256.txt.asc \  
&& grep " node-v$NODE_VERSION-linux-x64.tar.gz\$" SHASUMS256.txt.asc |
sha256sum -c - \  
&& tar -xzf "node-v$NODE_VERSION-linux-x64.tar.gz" -C /usr/local \--strip-
components=1 \  
&& rm "node-v$NODE_VERSION-linux-x64.tar.gz" SHASUMS256.txt.asc \  
&& npm install -g npm@"$NPM_VERSION" \  
&& npm cache clear  
  
WORKDIR /app  
  

