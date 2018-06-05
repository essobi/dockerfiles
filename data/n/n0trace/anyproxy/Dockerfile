FROM n0trace/yarn  
LABEL maintainer="n0trace@protonmail.com"  
  
RUN yarn global add anyproxy  
RUN yarn cache clean  
EXPOSE 8001 8002  
ENTRYPOINT anyproxy  

