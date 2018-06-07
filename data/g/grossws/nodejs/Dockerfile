FROM ubuntu:xenial  
MAINTAINER Konstantin Gribov <grossws@gmail.com>  
  
RUN apt-get update -y \  
&& apt-get install -y apt-transport-https curl \  
&& curl -s https://deb.nodesource.com/gpgkey/nodesource.gpg.key | apt-key add
\- \  
&& echo 'deb https://deb.nodesource.com/node_5.x xenial main' >
/etc/apt/sources.list.d/nodesource.list \  
&& apt-get update -y \  
&& apt-get install -y nodejs \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  

