FROM debian:wheezy  
  
MAINTAINER Purmode R <prdev@outlook.com>  
  
RUN echo "deb http://packages.hubzero.org/deb ellie-deb7 main" | tee -a
/etc/apt/sources.list  
RUN apt-key adv --keyserver pgp.mit.edu --recv-keys 143C99EF  
RUN apt-get update  
RUN echo "#!/bin/sh\nexit 0" > /usr/sbin/policy-rc.d  
RUN apt-get install -y apt-utils  
RUN apt-get upgrade -y  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y mysql-server  
RUN service mysql start && DEBIAN_FRONTEND=noninteractive apt-get install -y
hubzero-mysql  
RUN apt-get install -y hubzero-cms-2.0.0  
  
ENTRYPOINT ["/bin/bash"]  

