FROM nebo15/alpine-erlang:20.2.2  
MAINTAINER Nebo#15 support@nebo15.com  
# Important! Update this no-op ENV variable when this Dockerfile  
# is updated with the current date. It will force refresh of all  
# of the base images and things like `apt-get update` won't be using  
# old cached versions when the Dockerfile is built.  
ENV REFRESHED_AT=2018-01-13  
ENV LANG=en_US.UTF-8 \  
LANGUAGE=en_US:en \  
LC_ALL=en_US.UTF-8 \  
# Set this so that CTRL+G works properly  
TERM=xterm \  
HOME=/opt/app/ \  
ELIXIR_VERSION=1.6.4  
WORKDIR /tmp/elixir-build  
  
# Install Elixir  
RUN set -xe; \  
ELIXIR_DOWNLOAD_URL="https://github.com/elixir-
lang/elixir/releases/download/v${ELIXIR_VERSION}/Precompiled.zip" && \  
# Install Elixir build deps  
apk add \--no-cache --update --virtual .elixir-build \  
unzip \  
curl \  
ca-certificates && \  
# Download and validate Elixir checksum  
curl -fSL -o elixir-precompiled.zip "${ELIXIR_DOWNLOAD_URL}" && \  
unzip -d /usr/local elixir-precompiled.zip && \  
rm elixir-precompiled.zip && \  
# Install Hex and Rebar  
mix local.hex --force && \  
mix local.rebar --force && \  
cd /tmp && \  
rm -rf /tmp/elixir-build && \  
# Delete Elixir build deps  
apk del .elixir-build  
  
WORKDIR ${HOME}  
  
CMD ["iex"]  

