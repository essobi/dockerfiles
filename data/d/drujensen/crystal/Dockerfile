FROM ubuntu:16.04  
RUN apt-get update -qq  
  
RUN apt-get install -y --no-install-recommends build-essential curl ca-
certificates git vim netcat libyaml-0-2 libreadline-dev libxml2-dev  
  
RUN apt-get install -y --no-install-recommends libsqlite3-dev libpq-dev
libmysqlclient-dev  
  
ENV CRYSTAL_VERSION 0.24.1  
ENV CRYSTAL_REVISION 2  
RUN curl -L https://github.com/crystal-
lang/crystal/releases/download/v$CRYSTAL_VERSION/crystal-$CRYSTAL_VERSION-$CRYSTAL_REVISION-
linux-x86_64.tar.gz | tar xvz -C /opt/.  
  
ENV PATH /opt/crystal-$CRYSTAL_VERSION/bin:$PATH  
  
RUN mkdir -p /app  
WORKDIR /app  

