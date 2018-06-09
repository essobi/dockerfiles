FROM node:5  
ENV NPM_CONFIG_LOGLEVEL warn  
ENV PORT 8080  
ENV LOG_REQUESTS true  
ENV USE_GZIP true  
  
RUN npm install -g superstatic  
  
WORKDIR /data  
ADD index.html /data/index.html  
  
ONBUILD RUN rm /data/index.html  
ONBUILD ADD . /data  
  
EXPOSE $PORT  
ENTRYPOINT superstatic --host 0.0.0.0 --port $PORT \--gzip $USE_GZIP \--debug
$LOG_REQUESTS  

