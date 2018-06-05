FROM azukiapp/erlang:18  
MAINTAINER Azuki <support@azukiapp.com>  
  
ENV ELIXIR_VERSION=1.2.6  
# Install local Elixir hex and rebar  
RUN build_packages='curl' \  
set -x \  
&& apk --update add $build_packages \  
&& PRECOMPILED_ELIXIR_DIR="/tmp/elixir-v${ELIXIR_VERSION}-precompiled" \  
&& mkdir -p $PRECOMPILED_ELIXIR_DIR \  
&& cd $PRECOMPILED_ELIXIR_DIR \  
&& curl -sL https://github.com/elixir-
lang/elixir/releases/download/v${ELIXIR_VERSION}/Precompiled.zip -o
Precompiled.zip \  
&& unzip Precompiled.zip \  
&& PRECOMPILED_ELIXIR_DIR="/tmp/elixir-v${ELIXIR_VERSION}-precompiled" \  
&& cd $PRECOMPILED_ELIXIR_DIR \  
&& mkdir -p /usr/lib/elixir \  
&& cp -R bin /usr/lib/elixir \  
&& cp -R lib /usr/lib/elixir \  
&& ln -s /usr/lib/elixir/bin/elixir /usr/bin/elixir \  
&& ln -s /usr/lib/elixir/bin/elixirc /usr/bin/elixirc \  
&& ln -s /usr/lib/elixir/bin/iex /usr/bin/iex \  
&& ln -s /usr/lib/elixir/bin/mix /usr/bin/mix \  
&& mix local.hex --force \  
&& mix local.rebar --force \  
&& apk del --purge $build_packages \  
&& rm -rf /var/cache/apk/* /var/tmp/* /tmp/*  
  
CMD ["iex"]  

