FROM firstandthird/node:6.10-3-onbuild  
  
USER root  
RUN apk --update --no-cache --virtual add iputils  
RUN mkdir -p $HOME/log && chown node:node -R $HOME/log  
USER node  
  
ENV LOG_PATH $HOME/log/healthcheck.json  
  
EXPOSE 8080  
  

