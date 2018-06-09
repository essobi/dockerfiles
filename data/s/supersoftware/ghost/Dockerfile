FROM ghost:1.18-alpine  
  
# install custom theme  
RUN apk add --no-cache curl  
  
# install s3 adapter  
RUN npm install ghost-storage-adapter-s3  
  
# We cannot copy the s3 adapter inside content because  
# the parent image is exposing it as VOLUME.  
# Hence we copy the adapter within a custom entrypoint.sh  
COPY entrypoint.sh /usr/local/bin  
ENTRYPOINT ["entrypoint.sh"]  
CMD ["node", "current/index.js"]  

