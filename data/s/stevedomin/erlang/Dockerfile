FROM debian:jessie  
MAINTAINER Steve Domin <steve@stevedomin.com>  
  
RUN apt-get update && apt-get install -y wget  
  
RUN echo "deb http://packages.erlang-solutions.com/debian jessie contrib" >>
/etc/apt/sources.list  
RUN wget http://packages.erlang-solutions.com/ubuntu/erlang_solutions.asc &&
apt-key add erlang_solutions.asc  
  
RUN apt-get update && apt-get install -y \  
erlang=1:19.0-1 \  
erlang-base-hipe=1:19.0-1  
  
CMD ["erl"]  

