########################  
###### Build image #####  
########################  
FROM elixir:1.6-slim as builder  
  
LABEL maintainer=https://github.com/qgadrian  
  
RUN \  
mix local.hex --force \  
&& mix local.rebar --force \  
&& mix hex.info  
  
ADD . .  
  
RUN mix deps.get  
  
RUN mix build  
  
########################  
##### Runtime image ####  
########################  
FROM elixir:1.6-slim  
  
LABEL maintainer=https://github.com/qgadrian  
  
RUN mkdir -p /app  
  
COPY --from=builder ./smokex /app  
  
ENV PATH="/app:${PATH}"  
  
WORKDIR /app  
  
CMD ["/bin/bash"]  

