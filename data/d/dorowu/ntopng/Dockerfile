FROM ubuntu:14.04.2  
MAINTAINER Doro Wu <fcwu.tw@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update \  
&& apt-get install -y \--force-yes --no-install-recommends curl \  
&& curl -s --remote-name http://www.nmon.net/apt-stable/14.04/all/apt-ntop-
stable.deb \  
&& dpkg -i apt-ntop-stable.deb \  
&& rm apt-ntop-stable.deb \  
&& apt-get update \  
&& apt-get install -y \--force-yes ntopng libzmq3 libhiredis0.10 libnuma1 \  
&& apt-get autoclean \  
&& apt-get autoremove \  
&& rm -rf /var/lib/apt/lists/*  
  
EXPOSE 3000  
ENTRYPOINT ["/usr/bin/ntopng"]  

