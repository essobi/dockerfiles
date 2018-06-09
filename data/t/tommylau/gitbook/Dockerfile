FROM node:slim  
  
MAINTAINER Tommy Lau <tommy@gen-new.com>  
  
# Install GitBook  
RUN npm install gitbook-cli -g  
  
# Enable GitBook to output PDF file  
RUN apt-get update && apt-get install -y calibre git && rm -rf
/var/lib/apt/lists/*  
  
# Prepare work directory  
RUN mkdir /gitbook  
WORKDIR /gitbook  
  
EXPOSE 4000  
CMD ["gitbook", "serve", "/gitbook"]  

