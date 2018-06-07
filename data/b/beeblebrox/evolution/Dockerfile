FROM ubuntu:15.10  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -qqy sudo
evolution evolution-ews gnome-keyring && rm -rf /var/lib/apt/lists/* /tmp/*
/var/tmp/*  
  
VOLUME ["/home/developer"]  
  
RUN mkdir -p /home/developer  
  
ENV HOME=/home/developer  
ENTRYPOINT ["/usr/bin/evolution"]  
  

