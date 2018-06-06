FROM ruby:2.2.3  
MAINTAINER Diego Alves <dfqalves@gmail.com>  
  
RUN apt-get update -qq && apt-get install -y build-essential libpq-dev libaio1
unzip  
  
RUN mkdir /opt/oracle  
ADD *.zip /opt/oracle/  
RUN cd /opt/oracle && unzip -q \\*.zip  
RUN cd /opt/oracle/instantclient_12_1 && ln -s libclntsh.so.12.1 libclntsh.so  
ENV LD_LIBRARY_PATH /opt/oracle/instantclient_12_1  
  
RUN gem install ruby-oci8  

