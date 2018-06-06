FROM node:carbon  
  
ENV TMPDIR=/tmp/app  
ENV APPDIR=/app  
  
## stuff that can be cached:  
RUN mkdir -p $TMPDIR  
ADD package.json $TMPDIR  
RUN cd $TMPDIR && npm install  
RUN npm -g install http-server  
  
ADD . $TMPDIR  
WORKDIR $TMPDIR  
RUN npm run build  
  
RUN mv dist $APPDIR  
RUN rm -rf $TMPDIR  
  
WORKDIR $APPDIR  
  
CMD http-server  

