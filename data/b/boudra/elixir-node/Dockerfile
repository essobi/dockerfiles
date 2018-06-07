FROM ubuntu:bionic  
  
ENV LANG=C.UTF-8  
WORKDIR /elixir  
  
RUN apt-get update && \  
apt-get install --force-yes -y --no-install-recommends \  
openssh-client \  
ca-certificates \  
curl \  
git \  
build-essential \  
zlib1g-dev \  
liblzma-dev \  
pkg-config \  
mysql-client \  
xfonts-base \  
xfonts-75dpi \  
rlwrap \  
gnupg \  
netbase \  
wget \  
ruby \  
ruby-dev \  
unzip \  
python-minimal \  
libwxgtk3.0-0v5 \  
libsctp1 \  
g++ && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \  
wget https://packages.erlang-solutions.com/erlang/esl-
erlang/FLAVOUR_1_general/esl-erlang_20.3-1~ubuntu~bionic_amd64.deb && \  
dpkg -i esl-erlang_20.3-1~ubuntu~bionic_amd64.deb && \  
wget -q https://github.com/elixir-
lang/elixir/releases/download/v1.6.3/Precompiled.zip && \  
unzip Precompiled.zip && \  
rm -f Precompiled.zip && \  
ln -s /elixir/bin/elixirc /usr/local/bin/elixirc && \  
ln -s /elixir/bin/elixir /usr/local/bin/elixir && \  
ln -s /elixir/bin/mix /usr/local/bin/mix && \  
ln -s /elixir/bin/iex /usr/local/bin/iex && \  
/usr/local/bin/mix local.hex --force && \  
/usr/local/bin/mix local.rebar --force && \  
wget
https://deb.nodesource.com/node_8.x/pool/main/n/nodejs/nodejs_8.7.0-1nodesource1_amd64.deb
--no-check-certificate && \  
dpkg -i nodejs_8.7.0-1nodesource1_amd64.deb && \  
rm nodejs_8.7.0-1nodesource1_amd64.deb && \  
echo "prefix = ${HOME}/.node" > ~/.npmrc && \  
PATH="$HOME/.node/bin:$PATH"  
  
RUN gem install bundler  
  
CMD ["bin/bash"]  

