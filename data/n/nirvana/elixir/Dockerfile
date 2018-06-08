FROM nifty/erlang:latest  
  
MAINTAINER Nate West <natescott.west@gmail.com>  
  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
RUN apt-get update && apt-get install -y git elixir  
  
CMD ["iex"]  

