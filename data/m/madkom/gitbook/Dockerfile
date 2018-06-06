FROM node:latest  
  
MAINTAINER Michał Brzuchalski <m.brzuchalski@madkom.pl>  
  
LABEL version="2.5.2"  
  
RUN npm install -g gitbook-cli && gitbook versions:install 2.5.2 && \  
apt-get clean autoclean && npm cache clear && \  
rm -rf /tmp/* /var/lib/{apt,dpkg,cache,log}/*  
  
RUN apt-get update && apt-get install -yqq --no-install-recommends calibre git
&& \  
apt-get clean autoclean && \  
rm -rf /tmp/* /var/lib/{apt,dpkg,cache,log}/*  
  
WORKDIR /data  
  
VOLUME /data  
  
EXPOSE 4000 35729  
ENTRYPOINT ["gitbook"]  
CMD ["serve", "/data"]  

