FROM ubuntu:xenial  
  
MAINTAINER Félix Sanz <me@felixsanz.com>  
  
RUN apt-get update \  
&& apt-get install -y \--no-install-recommends curl gcc net-tools python-dev \  
&& curl -L http://www.aerospike.com/download/amc/3.6.13/artifact/ubuntu12 -o
aerospike-amc.deb \  
&& dpkg -i aerospike-amc.deb \  
&& rm aerospike-amc.deb \  
&& apt-get purge -y \--auto-remove curl \  
&& rm -rf /var/lib/apt/lists/*  
  
EXPOSE 8081  
  
CMD /usr/sbin/service amc start && tail -f /var/log/amc/*.log  

