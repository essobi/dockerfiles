# Docker image for citeproc-node app  
# Usage: $ docker run -d -p 8085:8085 -t {this image}  
# Pull base image.  
FROM node  
MAINTAINER Vitali Peil  
  
# append nodejs binaries TO PATH  
ENV PATH node_modules/.bin:$PATH  
  
# XML to JSON for optimal performance  
#RUN ./xmltojson.py ./csl ./csl-json  
#RUN ./xmltojson.py ./csl-locales ./csl-locales-json  
# Add source  
ADD . /src  
  
# Set Working directory  
WORKDIR /src  
  
# Expose port  
EXPOSE 8085  
# run app  
CMD ["node", "lib/citeServer.js"]  

