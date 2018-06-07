FROM mhart/alpine-node:latest  
MAINTAINER Alex Kern <alex@pavlovml.com>  
  
# install  
RUN npm install kue  
  
# cleanup  
RUN rm -rf /tmp/* /var/cache/apk/* /root/.npm /root/.npmrc /root/.node-gyp  
  
# run  
EXPOSE 3000  
CMD /node_modules/kue/bin/kue-dashboard -r $REDIS_URL  

