FROM marcelocg/phoenix  
LABEL maintainer="krdevmail@gmail.com"  
  
RUN apt-get update && apt-get install -y --force-yes build-essential  
RUN mix local.rebar --force  
RUN mix local.hex --force  
  
EXPOSE 80 4000  

