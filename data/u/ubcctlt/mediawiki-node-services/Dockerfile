FROM node:7-alpine  
  
ENV LOG_LEVEL info  
  
COPY . /src  
  
WORKDIR /src  
  
RUN apk add --no-cache git librsvg librsvg-dev build-base \  
&& npm install --only=production \  
&& npm cache clean --force \  
&& rm -rf /tmp/npm* /root/.node* /root/.npm  
  
RUN mkdir -p /data  
  
EXPOSE 7231 8142  
ENTRYPOINT ["./docker-entrypoint.sh"]  
  
CMD ["node", "server", "-c", "config.yaml"]  

