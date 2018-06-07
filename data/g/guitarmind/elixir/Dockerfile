FROM sinorga/alpine-erlang:19.3.4-DBG  
MAINTAINER Mark Peng <markpeng@exosite.com>  
  
ENV ELIXIR_VERSION 1.4.5  
RUN apk --update add --virtual build-dependencies wget ca-certificates && \  
wget --no-check-certificate https://github.com/elixir-
lang/elixir/releases/download/v${ELIXIR_VERSION}/Precompiled.zip && \  
mkdir -p /opt/elixir-${ELIXIR_VERSION}/ && \  
unzip Precompiled.zip -d /opt/elixir-${ELIXIR_VERSION}/ && \  
rm Precompiled.zip && \  
apk del build-dependencies && \  
rm -rf /etc/ssl && \  
rm -rf /var/cache/apk/*  
  
ENV PATH $PATH:/opt/elixir-${ELIXIR_VERSION}/bin  
  
RUN mix local.hex --force && \  
mix local.rebar --force  
  
CMD ["/bin/sh"]  

