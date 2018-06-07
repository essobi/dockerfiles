FROM ubuntu:trusty  
  
MAINTAINER Nate West <natescott.west@gmail.com>  
  
RUN apt-get update && apt-get -y upgrade && apt-get -y install wget  
  
RUN cd /tmp; wget https://packages.erlang-solutions.com/erlang-
solutions_1.0_all.deb && \  
dpkg -i erlang-solutions_1.0_all.deb  
  
RUN apt-get update && apt-get -y install erlang erlang-base-hipe build-
essential  
  
CMD ["erl"]  

