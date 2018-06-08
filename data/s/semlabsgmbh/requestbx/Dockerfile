FROM elixir:1.5.2  
ENV DEBIAN_FRONTEND=noninteractive  
  
ARG ENV=prod  
ARG PORT=4002  
ENV MIX_ENV=$ENV REPLACE_OS_VARS=true  
ENV PORT=$PORT  
  
COPY . /app/  
WORKDIR /app  
  
RUN rm -rf _build \  
&& rm -rf deps  
  
# Install hex & rebar  
RUN mix do \  
local.rebar --force, \  
local.hex --force, \  
deps.clean --all, \  
deps.get, \  
compile  
  
#HTTP  
EXPOSE 4002  
# Finally run the server  
CMD elixir -S mix phx.server  

