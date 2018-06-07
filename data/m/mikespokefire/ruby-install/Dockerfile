FROM mikespokefire/ubuntu-base:latest  
MAINTAINER Michael Smith <mike@spokefire.co.uk>  
  
RUN apt-get install -y build-essential wget  
  
RUN wget -O ruby-install-0.5.0.tar.gz https://github.com/postmodern/ruby-
install/archive/v0.5.0.tar.gz  
RUN tar -xzvf ruby-install-0.5.0.tar.gz  
WORKDIR ruby-install-0.5.0  
RUN make install  

