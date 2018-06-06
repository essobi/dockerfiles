FROM bitwalker/alpine-elixir-phoenix:latest  
MAINTAINER Eoin Houlihan <ehoulih@tcd.ie>  
  
# Set exposed ports  
EXPOSE 4000  
ENV PORT=4000 MIX_ENV=prod  
  
# Cache elixir deps  
ADD mix.exs mix.lock ./  
RUN mix do deps.get, deps.compile  
  
# Same with npm deps  
ADD package.json package.json  
RUN npm install  
  
ADD . .  
  
# Run frontend build, compile, and digest assets  
RUN brunch build --production && \  
mix do compile, phoenix.digest  
  
CMD ["mix", "phoenix.server"]

