FROM ubuntu:trusty  
MAINTAINER Scott Chamberlain <myrmecocystus@gmail.com>  
  
RUN sudo apt-get -y update  
RUN sudo apt-get -y upgrade  
RUN sudo apt-get install -y sqlite3 libsqlite3-dev  
  
RUN apt-get update && apt-get install -y wget \  
&& wget -q https://s3-us-west-2.amazonaws.com/gbif-backbone/gbif.sqlite  

