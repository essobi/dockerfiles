FROM elixir:1.4  
  
ENV PJS_URL
https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2  
  
RUN apt-get update && \  
apt-get install -y build-essential erlang-dev git-core && \  
mix local.hex --force && \  
mix local.rebar --force && \  
mkdir -p /tmp/phantomjs && \  
curl --silent -L ${PJS_URL} | tar -xj --strip-components=1 -C /tmp/phantomjs
&& \  
mv /tmp/phantomjs/bin/phantomjs /usr/local/bin && \  
curl -sL https://deb.nodesource.com/setup_7.x | bash - && \  
apt-get install -y nodejs && \  
npm install -g brunch && \  
rm -rf /tmp/phantomjs /var/lib/apt/lists/*  

