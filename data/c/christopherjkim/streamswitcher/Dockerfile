FROM elixir:1.6.4  
EXPOSE 4000  
RUN echo "deb http://http.debian.net/debian jessie-backports main contrib non-
free" >> /etc/apt/sources.list  
  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -  
RUN apt-get install -y -q --no-install-recommends nodejs imagemagick ffmpeg  
  
RUN mix local.hex --force && mix local.rebar --force  
RUN mkdir -p /app  
WORKDIR /app  
  
COPY mix.exs /app  
COPY mix.lock /app  
RUN mix deps.get --only prod  
  
COPY assets/package.json /app/assets/package.json  
RUN cd assets && npm install  
  
COPY . /app  
RUN MIX_ENV=prod mix compile  
RUN cd assets && node node_modules/brunch/bin/brunch build --production  
RUN MIX_ENV=prod mix phx.digest  
  
ARG port=4000  
ENV PORT $port  
  
CMD MIX_ENV=prod mix phx.server  

