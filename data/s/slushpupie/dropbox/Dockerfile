FROM ubuntu:latest  
MAINTAINER Jay Kline <jay@slushpupie.com>  
  
RUN apt-get update && apt-get install -y curl python-software-properties && rm
-rf /tmp/* /var/tmp/* /var/cache/apt/archives/* /var/lib/apt/lists/*  
  
RUN cd ~ && curl -L "https://www.dropbox.com/download?plat=lnx.x86_64" | tar
xzf -  
RUN curl -Lo /usr/bin/dropbox.py
"https://www.dropbox.com/download?dl=packages/dropbox.py"  
RUN chmod +x /usr/bin/dropbox.py  
  
RUN mkdir -p /root/Dropbox  
  
WORKDIR /root  
  
VOLUME ["/root/Dropbox", "/root/.dropbox"]  
  
ENV TINI_VERSION v0.16.1  
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini
/tini  
RUN chmod +x /tini  
ENTRYPOINT ["/tini", "--"]  
  
CMD ["/root/.dropbox-dist/dropboxd"]  

