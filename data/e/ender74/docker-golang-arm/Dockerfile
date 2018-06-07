FROM resin/armv7hf-debian:sid  
MAINTAINER Heiko Hüter <ender@ender74.de>  
  
RUN apt-get update -y \  
&& apt-get upgrade -y \  
&& apt-get install --no-install-recommends -y curl ca-certificates golang -y \  
&& apt-get autoremove -y \  
&& apt-get clean -y \  
&& rm -rf /var/lib/apt/lists/* /root/.cache  

