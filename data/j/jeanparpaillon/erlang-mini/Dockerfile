FROM debian:jessie  
MAINTAINER Jean Parpaillon <jean.parpaillon@free.fr>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update  
  
RUN apt-get -y install --no-install-recommends \  
erlang-base erlang-dev erlang-crypto erlang-parsetools erlang-ssh erlang-ssl
erlang-tools erlang-mnesia \  
erlang-eunit erlang-parsetools erlang-syntax-tools\  
ca-certificates && \  
apt-get clean  
  
CMD [ "/usr/bin/erl" ]  

