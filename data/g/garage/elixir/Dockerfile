FROM garage/erlang  
  
MAINTAINER Reinaldo Junior <juniorz@gmail.com>  
  
RUN apt-get update && apt-get upgrade -y  
  
## Checks for compatible Erlang version  
RUN erl -noshell -eval 'io:fwrite("~s~n", [erlang:system_info(otp_release)]).'
-s erlang halt | grep -q '^R1[6789]'  
  
## Build and Install Elixir  
RUN /var/garage/install make git-core &&\  
curl -k -L https://github.com/elixir-lang/elixir/archive/stable.tar.gz | tar
-C /tmp/ -xzvf - &&\  
cd /tmp/elixir-stable &&\  
make clean test &&\  
make install  
  
RUN apt-get purge -y make  
  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENV GARAGE_PROVIDES elixir elixirc iex mix  

