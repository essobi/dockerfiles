FROM debian:jessie  
MAINTAINER Paul Andrew Liljenberg "liljenberg.paul@gmail.com"  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && apt-get -y install \  
git-core \  
make \  
sudo \  
build-essential  
  
RUN git clone git://git.code.sf.net/p/crunch-wordlist/code crunch && \  
cd crunch && \  
make && \  
make install  
  
ADD crunch.sh /  
VOLUME /data  
WORKDIR /data  
  
ENTRYPOINT ["/crunch.sh"]  

