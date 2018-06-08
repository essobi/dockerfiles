FROM ubuntu:xenial  
MAINTAINER Hartman Tam <hartmantam@gmail.com>  
  
LABEL version="0.1-beta-1"  
LABEL description="A simple yet flexible stunnel docker for fast deployment"  
  
RUN apt-get -q update && \  
apt-get -qy install stunnel4 && \  
apt-get -y autoremove && \  
apt-get -y clean && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /tmp/*  
  
ENTRYPOINT [ "stunnel" ]  
CMD [ "/config" ]

