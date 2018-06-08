FROM ruby:latest  
MAINTAINER Rhuan Barreto <rhuan@rhuan.com.br>  
  
EXPOSE 80  
# Setup FreeTDS  
RUN apt-get update -qq && apt-get install -y --no-install-recommends build-
essential libpq-dev nodejs libc6-dev  
RUN wget ftp://ftp.freetds.org/pub/freetds/stable/freetds-1.00.27.tar.gz && \  
tar -xzf freetds-1.00.27.tar.gz && \  
cd freetds-1.00.27 && \  
./configure --prefix=/usr/local \--with-tdsver=7.3 && \  
make && \  
make install  

