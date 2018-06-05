FROM node:argon  
  
RUN git clone https://github.com/etsy/statsd.git \  
&& git clone https://github.com/wowgroup/statsd-cloudwatch.git
statsd/backends/cloudwatch \  
&& (cd /statsd/backends/cloudwatch && npm install) \  
&& curl -o /bin/gosu -fsSL
https://github.com/tianon/gosu/releases/download/1.8/gosu-amd64 \  
&& curl -o /bin/tini -fsSL
https://github.com/krallin/tini/releases/download/v0.9.0/tini \  
&& chmod +x /bin/gosu /bin/tini  
ADD config.js /etc/statsd.js  
  
EXPOSE 8125/udp 8126  
WORKDIR /statsd  
ENTRYPOINT ["/bin/tini", "--", "/bin/gosu", "nobody"]  
CMD ["node", "stats.js", "/etc/statsd.js"]  

