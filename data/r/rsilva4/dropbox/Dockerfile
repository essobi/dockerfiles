FROM debian:stretch  
LABEL maintainer="@rcsilva4"  
  
RUN useradd -m -s /bin/bash -p '*' dropbox  
WORKDIR /home/dropbox  
  
RUN apt-get update && apt-get install -y wget libglib2.0-0  
  
USER dropbox  
RUN cd ~ && wget -O - "https://www.dropbox.com/download?plat=lnx.x86_64" | tar
xzf -  
  
USER root  
RUN apt-get purge -y wget && apt-get clean && rm -rf /var/lib/apt/lists/*
/tmp/* /var/tmp/*  
  
USER dropbox  
  
VOLUME /home/dropbox  
  
ENTRYPOINT ["/home/dropbox/.dropbox-dist/dropboxd"]  

