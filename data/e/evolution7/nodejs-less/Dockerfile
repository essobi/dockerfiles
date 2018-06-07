# Build:  
# docker build -t evolution7/nodejs-less .  
#  
# Run:  
# docker run --rm -v `pwd`:/app -ti evolution7/nodejs-less styles.less >
styles.css  
FROM node:latest  
RUN npm install -g less  
RUN npm install -g less-plugin-clean-css  
  
VOLUME ["/app"]  
WORKDIR /app  
  
ENTRYPOINT ["/usr/local/bin/lessc"]  

