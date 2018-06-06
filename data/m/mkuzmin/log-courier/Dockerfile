FROM ubuntu  
MAINTAINER Michael Kuzmin <mkuzmin@gmail.com>  
  
RUN \  
export DEBIAN_FRONTEND=noninteractive \  
&& apt-get -qq update \  
&& apt-get install -y software-properties-common \  
&& add-apt-repository ppa:devel-k/log-courier \  
&& apt-get -qq update \  
&& apt-get install -y log-courier \  
&& apt-get -y purge --auto-remove software-properties-common \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
ENTRYPOINT ["/usr/sbin/log-courier"]  

