# Inherit from Heroku's stack  
FROM heroku/heroku:16  
MAINTAINER Bob Olde Hampsink <b.oldehampsink@nerds.company>  
  
# Internally, we arbitrarily use port 3000  
ENV PORT 3000  
# Which versions?  
ENV ERLANG_MAJOR_VERSION 20  
ENV ERLANG_VERSION 20.2.4  
ENV ELIXIR_VERSION 1.6.3  
ENV NODE_ENGINE 8.10.0  
ENV LC_ALL en_US.UTF-8  
ENV SECRET_KEY_BASE $(openssl rand -base64 32)  
  
# Create some needed directories  
RUN mkdir -p /app/.heroku/erlang /app/.heroku/elixir /app/.heroku/node
/app/.profile.d  
WORKDIR /app/user  
  
# Locate our binaries  
ENV PATH
/app/.heroku/erlang/bin:/app/.heroku/elixir/bin:/app/.heroku/node/bin/:/app/user/node_modules/.bin:$PATH  
  
# Install Erlang  
RUN curl --silent --location https://s3.amazonaws.com/heroku-buildpack-
elixir/erlang/cedar-14/OTP-$ERLANG_VERSION.tar.gz | tar xz -C
/app/.heroku/erlang --strip=1  
RUN /app/.heroku/erlang/Install -minimal /app/.heroku/erlang  
  
# Install Elixir  
RUN curl --silent --location
https://repo.hex.pm/builds/elixir/v$ELIXIR_VERSION-
otp-$ERLANG_MAJOR_VERSION.zip -o /tmp/elixir.zip  
RUN unzip -q /tmp/elixir.zip -d /app/.heroku/elixir  
RUN rm -rf /tmp/elixir.zip  
  
# Install dependencies  
RUN mix local.hex --force  
RUN mix local.rebar --force  
  
# Install Node  
RUN curl -s
https://s3pository.heroku.com/node/v$NODE_ENGINE/node-v$NODE_ENGINE-
linux-x64.tar.gz | tar --strip-components=1 -xz -C /app/.heroku/node  
  
# Add source for yarn  
RUN curl -sS http://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -  
RUN echo "deb http://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list  
  
# Install dependencies  
RUN apt-get update && apt-get install -y yarn  
  
# copy dep files first so Docker caches the install step if they don't change  
ONBUILD COPY mix.lock /app/user/  
ONBUILD COPY mix.exs /app/user/  
# run install  
ONBUILD RUN mix deps.get  
  
# run npm or yarn install  
# add yarn.lock to .slugignore in your project  
ONBUILD COPY package*.json yarn.* /app/user/  
ONBUILD RUN [ -f yarn.lock ] && yarn install --no-progress || npm install  
  
# rest of app  
ONBUILD COPY . /app/user/  

