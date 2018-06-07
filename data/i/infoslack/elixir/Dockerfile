FROM infoslack/erlang  
  
MAINTAINER Daniel Romero <infoslack@gmail.com>  
  
ENV ELIXIR_VERSION=1.1.1  
  
RUN set -xe \  
&& buildDeps=' \  
autoconf \  
bison \  
ca-certificates \  
curl \  
gcc \  
g++ \  
libbz2-dev \  
libgdbm-dev \  
libglib2.0-dev \  
libncurses-dev \  
libodbc1 \  
libreadline-dev \  
libssl-dev \  
libxml2-dev \  
libxslt-dev \  
unixodbc-dev \  
make \  
' \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends $buildDeps \  
&& curl -SL "https://github.com/elixir-
lang/elixir/archive/v$ELIXIR_VERSION.tar.gz" -o elixir.tar.gz \  
&& mkdir -p /usr/src/elixir \  
&& tar -xvf elixir.tar.gz -C /usr/src/elixir --strip-components=1 \  
&& rm elixir.tar.gz \  
&& cd /usr/src/elixir \  
&& make -j$(nproc) clean install \  
&& rm -rf /usr/src/elixir \  
&& apt-get purge -y --auto-remove $buildDeps \  
&& rm -rf /var/lib/apt/lists/*  
  
CMD ["mix"]  

