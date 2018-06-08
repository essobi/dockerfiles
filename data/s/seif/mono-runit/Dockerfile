FROM seif/mono  
  
MAINTAINER Seif Attar <iam@seifattar.net>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update \  
&& apt-get install runit -y --no-install-recommends \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /var/tmp/*  
  
ENTRYPOINT ["/usr/sbin/runsvdir-start"]  

