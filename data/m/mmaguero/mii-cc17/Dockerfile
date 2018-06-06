FROM bitnami/apache:latest  
MAINTAINER Marvin Agüero "marvin-aguero@hotmail.com"  
RUN apt-get -y update && apt-get -y upgrade  
  
RUN apt-get install -y apt-utils && apt-get install -y perl \  
build-essential libdancer-perl libdbd-mysql-perl cpanminus vim  
RUN cpanm Dancer::Plugin::SimpleCRUD && cpanm Dancer::Plugin::Auth::Extensible  
  
RUN apt-get autoclean && apt-get clean && apt-get autoremove  
  
EXPOSE 14000 80 443  

