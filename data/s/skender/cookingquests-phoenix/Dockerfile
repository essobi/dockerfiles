FROM elixir:latest  
ENV DEBIAN_FRONTEND=noninteractive  
ENV MIX_ENV=prod  
ENV REPLACE_OS_VARS=true  
  
RUN mix local.rebar --force  
RUN mix local.hex --force  
RUN apt-get update && apt-get install -y unzip  
ADD https://github.com/CookingQuest/phoenix/archive/master.zip /repo/repo.zip  
WORKDIR /repo  
RUN unzip repo.zip  
WORKDIR /repo/phoenix-master  
  
RUN mix do deps.get, deps.compile, compile, release --verbose --env=prod  
WORKDIR /repo  
RUN tar -xzf phoenix-
master/_build/prod/rel/cooking_quest/releases/0.0.1/cooking_quest.tar.gz  
RUN rm -rf phoenix-master  
  
EXPOSE 4000  
CMD ./bin/cooking_quest foreground

