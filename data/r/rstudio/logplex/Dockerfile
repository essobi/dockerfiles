FROM ubuntu:trusty  
  
RUN apt-get update -qq && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y \  
build-essential \  
erlang-dev \  
erlang-nox \  
git  
  
RUN mkdir /opt/logplex  
WORKDIR /opt/logplex  
COPY . /opt/logplex  
  
# configure logplex  
RUN ./rebar --config public.rebar.config get-deps compile  
  
EXPOSE 8001 8601  
# Set the entry point script  
ENTRYPOINT ["/opt/logplex/entrypoint.bash"]  
  
CMD ["bin/logplex"]  

