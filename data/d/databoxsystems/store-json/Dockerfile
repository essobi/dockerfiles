FROM alpine:edge  
  
RUN \  
echo http://dl-4.alpinelinux.org/alpine/edge/testing >> /etc/apk/repositories
&& \  
apk add --no-cache mongodb && \  
apk add --no-cache nodejs nodejs-npm && \  
rm /usr/bin/mongoperf  
  
VOLUME /database  
  
#ADD package.json package.json  
ADD . .  
RUN npm install && npm run clean  
  
LABEL databox.type="store"  
  
EXPOSE 8080  
#Next 3 lines are neded to pass tests only  
RUN mkdir -p /run/secrets  
RUN touch /run/secrets/ARBITER_TOKEN  
RUN touch /run/secrets/DATABOX_ROOT_CA  
  
CMD ["npm","start"]  

