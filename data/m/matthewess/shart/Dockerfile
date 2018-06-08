# base image  
FROM elixir:alpine  
  
LABEL author="mat <mess@yelp.com>"  
  
WORKDIR /app  
  
ADD . /app  
  
ENV MIX_ENV prod  
  
RUN export SHART_SECRET_KEY=$(mix run utils/random.exs)  
  
RUN mix local.hex --force  
RUN mix local.rebar --force  
RUN mix deps.get  
RUN apk update && apk add nodejs nodejs-npm  
RUN cd assets && npm install  
RUN mix release  
  
CMD ["_build/prod/rel/shart/bin/shart", "start"]  

