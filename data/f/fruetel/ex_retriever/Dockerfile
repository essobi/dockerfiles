FROM elixir:1.6.2-slim  
  
RUN apt-get update && apt-get -y install git  
RUN mix local.hex --force  
RUN mix local.rebar --force  
  
WORKDIR /code  
  
COPY ./mix.exs /code/  
COPY ./mix.lock /code/  
  
ENV MIX_ENV test  
RUN mix deps.get  
  
ENV MIX_ENV prod  
RUN mix deps.get  
  
COPY . /code  
  
ENTRYPOINT ["./docker-entrypoint.sh"]  
CMD ["run"]  

