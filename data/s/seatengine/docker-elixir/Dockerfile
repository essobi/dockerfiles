FROM erlang:20-alpine  
  
# elixir expects utf8.  
ENV ELIXIR_VERSION="v1.4.5" \  
LANG=C.UTF-8  
  
RUN set -xe \  
&& ELIXIR_DOWNLOAD_URL="https://github.com/elixir-
lang/elixir/releases/download/v1.4.5/Precompiled.zip" \  
&&
ELIXIR_DOWNLOAD_SHA256="a740e634e3c68b1477e16d75a0fd400237a46c62ceb5d04551dbc46093a03f98"
\  
&& buildDeps=' \  
ca-certificates \  
curl \  
unzip \  
' \  
&& apk update --no-cache \  
&& apk add \--no-cache ca-certificates curl unzip \  
&& curl -fSL -o elixir-precompiled.zip $ELIXIR_DOWNLOAD_URL \  
&& unzip -d /usr/local elixir-precompiled.zip \  
&& rm elixir-precompiled.zip && \  
apk add nodejs make libc-dev gcc git bash && \  
mix local.hex --force && mix local.rebar --force  
  
CMD ["iex"]  

