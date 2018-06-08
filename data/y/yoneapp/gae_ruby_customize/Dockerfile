# Use the base image provided by Google  
FROM gcr.io/google_appengine/ruby  
  
# Install wget  
# https://github.com/phusion/baseimage-docker/issues/319  
RUN apt-get update  
RUN apt-get update && apt-get install -y --no-install-recommends apt-utils  
RUN apt-get -y install wget  
  
# Install libgraphqlparser  
RUN apt-get -y install cmake  
RUN wget https://github.com/graphql/libgraphqlparser/archive/v0.5.0.tar.gz  
RUN tar -xzvf v0.5.0.tar.gz  
RUN cd libgraphqlparser-0.5.0/ && cmake . && make && make install  
  
# Install ImageMagick  
RUN apt-get -y install ImageMagick  

