FROM ubuntu:14.04  
MAINTAINER Alexandre De Dommelin <adedommelin@tuxz.net>  
  
# Environment variables  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update  
RUN apt-get install -y locales  
  
RUN apt-get -y install phantomjs wget libpcap0.8  
RUN cd /usr/local/bin ; /usr/bin/wget
https://github.com/Shopify/minesweeper/releases/download/v0.1.1/minesweeper-0.1.1-linux-
amd64.tar.gz ; tar -xzvf minesweeper-0.1.1-linux-amd64.tar.gz ; rm -f
minesweeper-0.1.1-linux-amd64.tar.gz  
RUN chmod +x /usr/local/bin/minesweeper  
  
ENTRYPOINT [ "/usr/local/bin/minesweeper", "-v=true" ]  
  

