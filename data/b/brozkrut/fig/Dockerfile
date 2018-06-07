FROM ubuntu  
MAINTAINER Bartek Rozkrut <bartek@rozkrut.pl>  
  
# Update packages and install curl  
RUN apt-get update && apt-get install -y curl  
  
# Install latest docker  
RUN curl -sSL https://get.docker.com/ubuntu/ | sudo sh  
  
# Install latest fig  
RUN curl -L https://github.com/docker/fig/releases/download/1.0.0/fig-`uname
-s`-`uname -m` > /usr/local/bin/fig ; chmod +x /usr/local/bin/fig  
  
VOLUME ["/config"]  
WORKDIR /config  
  
# Default run "fig --help"  
ENTRYPOINT ["/usr/local/bin/fig"]  
CMD ["--help"]  

