FROM ubuntu  
MAINTAINER Tibor Sári <tiborsari@gmx.de>  
  
RUN apt-get update -qqy && \  
apt-get upgrade -qqy && \  
apt-get install --no-install-recommends -qqy \  
filezilla \  
&& \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
CMD filezilla

