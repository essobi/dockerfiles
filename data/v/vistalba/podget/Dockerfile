FROM ubuntu:xenial  
RUN apt-get update && apt-get install -y podget perl  
ENTRYPOINT ["/usr/bin/podget"]  
RUN apt-get autoremove -y && apt-get autoclean -y && rm -rf /var/cache/apt/*
/var/cache/debconf/* /var/lib/apt/* /var/lib/dpkg/* /tmp/* /var/tmp/*
/var/log/*  

