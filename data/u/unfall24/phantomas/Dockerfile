FROM node:6.8.0-slim  
  
RUN apt-get update && apt-get install -y libfontconfig1 bzip2  
  
RUN npm install --global --no-optional phantomas phantomjs-prebuilt@^2.1.5  
  
ENTRYPOINT ["phantomas"]  
  
CMD ["--help"]  

