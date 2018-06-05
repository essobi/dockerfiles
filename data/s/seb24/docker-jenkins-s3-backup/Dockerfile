FROM ubuntu:14.10  
MAINTAINER Lemarinel Sebastien <lemarinel.s@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update \  
&& apt-get install -yq --no-install-recommends python-pip \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -rf /tmp/* \  
&& pip install awscli  
  
ADD start.sh /start.sh  
  
ENTRYPOINT ["/start.sh"]  

