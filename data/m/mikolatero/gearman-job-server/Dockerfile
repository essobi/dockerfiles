## Trusty = Ubuntu 14.04  
FROM ubuntu:trusty  
  
## Ask nothing when install with apt or deb  
ENV DEBIAN_FRONTEND noninteractive  
  
## Install gearman from Ondřej Surý PPA  
RUN echo "deb http://ppa.launchpad.net/ondrej/php/ubuntu trusty main" >
/etc/apt/sources.list.d/php.list && \  
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E5267A6C && \  
apt-get update && \  
apt-get install -f -y gearman  
  
## Expose the standard port for gearman  
EXPOSE 4730  
## Run gearman foreground (we need -L 0.0.0.0 for avoid ipv6 bug)  
CMD gearmand -p 4730 -L 0.0.0.0  

