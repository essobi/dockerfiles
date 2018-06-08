FROM erlang:19  
# elixir expects utf8.  
ENV ELIXIR_VERSION="v1.3.4" \  
LANG=C.UTF-8 \  
MIX_ENV=prod  
  
WORKDIR /app  
  
COPY . /app  
  
RUN set -xe \  
&& ELIXIR_DOWNLOAD_URL="https://github.com/elixir-
lang/elixir/releases/download/${ELIXIR_VERSION}/Precompiled.zip" \  
&&
ELIXIR_DOWNLOAD_SHA256="eac16c41b88e7293a31d6ca95b5d72eaec92349a1f16846344f7b88128587e10"\  
&& NODEJS_VERSION=6.9.2 \  
&& buildDeps=' \  
unzip \  
python \  
python-dev \  
python-pip \  
python-virtualenv \  
curl \  
ca-certificates \  
nginx \  
' \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends $buildDeps \  
&& curl -fSL -o node.tgz
https://nodejs.org/dist/v${NODEJS_VERSION}/node-v${NODEJS_VERSION}-linux-x64.tar.gz
\  
&& tar xf node.tgz -C /usr/local \--strip-components=1 \  
&& rm -f node.tgz /usr/local/*.md /usr/local/LICENSE \  
&& curl -fSL -o elixir-precompiled.zip $ELIXIR_DOWNLOAD_URL \  
&& echo "$ELIXIR_DOWNLOAD_SHA256 elixir-precompiled.zip" | sha256sum -c - \  
&& unzip -qq -d /usr/local elixir-precompiled.zip \  
&& rm elixir-precompiled.zip \  
&& pip install livestreamer \  
&& npm install request \  
&& mix local.hex --force \  
&& mix local.rebar --force \  
&& mix deps.get \  
&& mix compile \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \  
&& apt-get clean  
  
CMD service nginx start && epmd -daemon && elixir --no-halt -S mix  

