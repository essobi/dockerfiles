FROM elixir:1.6-slim  
  
EXPOSE 80  
ENV MIX_ENV prod  
ENV PORT 80  
WORKDIR /usr/src/points-api  
COPY . .  
  
RUN mix local.hex --force && mix local.rebar --force  
RUN mix deps.get && mix compile  
  
CMD ["mix", "phx.server"]  

