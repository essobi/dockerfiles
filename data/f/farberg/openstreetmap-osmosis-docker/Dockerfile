FROM debian:jessie  
  
MAINTAINER Dennis Pfisterer <github@farberg.de>  
  
RUN apt-get update && apt-get install -qq osmosis osmctools  
  
RUN mkdir /data  
  
VOLUME /data  
  
ENTRYPOINT ["osmosis"]  
  
CMD ["--help"]  

