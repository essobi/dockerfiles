FROM edib/base-erlang:19  
MAINTAINER Christoph Grabo <edib@markentier.com>  
  
#RUN apk --update add 'elixir<1.4.0' && rm -rf /var/cache/apk/*  
ENV ELIXIR_VERSION 1.3.3  
RUN curl -sSL https://github.com/elixir-
lang/elixir/releases/download/v${ELIXIR_VERSION}/Precompiled.zip \  
-o Precompiled.zip && \  
mkdir -p /opt/elixir-${ELIXIR_VERSION}/ && \  
unzip Precompiled.zip -d /opt/elixir-${ELIXIR_VERSION}/ && \  
rm Precompiled.zip  
  
ENV PATH $PATH:/opt/elixir-${ELIXIR_VERSION}/bin  
  
RUN mix local.hex --force && \  
mix local.rebar --force  

