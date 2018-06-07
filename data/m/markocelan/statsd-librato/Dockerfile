FROM node:0.12  
MAINTAINER marko.celan@gmail.com  
  
RUN mkdir -p /app && \  
cd /app && \  
curl -L https://github.com/etsy/statsd/tarball/master | tar -xz && \  
ln -s etsy-statsd-* statsd && \  
curl -L https://raw.githubusercontent.com/tomazk/statsd-librato-
backend/master/lib/librato.js > statsd/backends/librato.js  
  
ADD files/entrypoint.sh /  
RUN chmod +x /*.sh  
  
EXPOSE 8125/udp 8126  
ENTRYPOINT [ "/entrypoint.sh" ]  

