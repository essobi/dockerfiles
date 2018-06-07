FROM gliderlabs/alpine:3.2  
  
ENV USER root  
RUN apk --update add python nodejs bash  
  
EXPOSE 8125/udp  
EXPOSE 8125  
  
RUN npm install -g statsd statsd-librato-backend  
RUN mkdir -p /etc/statsd  
ADD ./config.js /etc/statsd/  
  
ENTRYPOINT ["statsd", "/etc/statsd/config.js"]  

