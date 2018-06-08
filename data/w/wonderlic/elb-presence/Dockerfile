FROM wonderlic/nodejs:0.12.0  
MAINTAINER Wonderlic DevOps <DevOps@wonderlic.com>  
  
COPY node_modules /app/node_modules  
COPY index.js /app/index.js  
  
RUN ln -s /usr/bin/node /app/elb-presence  
  
CMD ["/app/elb-presence", "/app/index.js"]  

