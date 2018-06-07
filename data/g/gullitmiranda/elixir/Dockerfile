FROM gullitmiranda/node  
MAINTAINER Gullit Miranda <gullitmiranda@gmail.com>  
  
ENV REPOSITORY=@testing  
ENV ELIXIR_VERSION=1.0.4  
# Install local Elixir hex and rebar  
RUN PRECOMPILED_ELIXIR_DIR="/tmp/elixir-v${ELIXIR_VERSION}-precompiled" \  
&& ERLANG=erlang17 \  
&& PKG_DEPS=" \  
${ERLANG}${REPOSITORY} ${ERLANG}-kernel${REPOSITORY}
${ERLANG}-stdlib${REPOSITORY} \  
${ERLANG}-compiler${REPOSITORY} ${ERLANG}-crypto${REPOSITORY} \  
${ERLANG}-syntax-tools${REPOSITORY} ${ERLANG}-inets${REPOSITORY}
${ERLANG}-ssl${REPOSITORY} \  
${ERLANG}-public-key${REPOSITORY} ${ERLANG}-asn1${REPOSITORY}
${ERLANG}-sasl${REPOSITORY} \  
${ERLANG}-erl-interface${REPOSITORY} ${ERLANG}-dev${REPOSITORY} \  
" \  
&& apk add --update $PKG_DEPS \  
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
&& rm -rf /var/cache/apk/* /var/tmp/* /tmp/*  
  
CMD ["iex"]  

