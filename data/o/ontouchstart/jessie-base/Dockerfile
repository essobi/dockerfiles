FROM debian:jessie  
MAINTAINER Sam Liu <ontouchstart@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update  
RUN apt-get -y upgrade  
  
RUN apt-get install -y apt-utils  
RUN apt-get install -y curl wget git  
RUN apt-get install -y build-essential python-software-properties ruby  
RUN apt-get install -y zlib1g-dev libpcre3-dev libbz2-dev libssl-dev libffi-
dev libreadline-dev libyaml-dev libsqlite3-dev libxml2-dev libxslt1-dev
libcurl4-openssl-dev  
RUN apt-get install -y bison autoconf pkg-config  
RUN apt-get install -y sqlite3  
RUN apt-get install -y vim  
RUN apt-get install -y groff  
ENV HOME /home  
WORKDIR /home  

