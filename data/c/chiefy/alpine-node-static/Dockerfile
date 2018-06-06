FROM mhart/alpine-node:latest  
  
MAINTAINER Christopher 'Chief' Najewicz <chief@beefdisciple.com>  
  
ENV PORT=3000 WORKDIR=/var/www  
  
RUN mkdir /app && cd app && npm install node-static  
  
RUN mkdir -p $WORKDIR \  
&& echo "<html><body><h1>Nothing to see here!</h1></body></html>" >
$WORKDIR/index.html  
  
ADD index.js /app/  
  
VOLUME $WORKDIR  
  
EXPOSE $PORT  
  
CMD node /app/index.js  

