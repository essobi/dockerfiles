FROM ubuntu:14.04  
MAINTAINER graham@grahamc.com  
  
RUN apt-get update  
RUN apt-get upgrade -y  
RUN apt-get install -y build-essential  
RUN apt-get install -y curl  
  
ADD https://github.com/postmodern/ruby-install/archive/v0.4.3.tar.gz
/tmp/ruby-install.tar.gz  
RUN tar -xzvf /tmp/ruby-install.tar.gz -C /tmp/  
RUN rm /tmp/ruby-install.tar.gz  
RUN mv /tmp/ruby-install* /tmp/ruby-install  
  
WORKDIR /tmp/ruby-install  
RUN make install  
  
WORKDIR /  
  

