FROM phusion/passenger-customizable:0.9.17  
MAINTAINER Hemslo <hemslo.wang@gmail.com>  
  
RUN /pd_build/ruby2.2.sh  
RUN apt-get update && apt-get install -y \  
libicu-dev \  
cmake \  
&& apt-get upgrade -y -o Dpkg::Options::="--force-confold" \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
RUN npm install -g bower  

