FROM node:4.7.3  
RUN npm install -g node-inspector@0.12.8 --unsafe-perm \  
&& npm cache clean && rm -rf /tmp/*  
  
ENV NODE_ENV development  
EXPOSE 8080  
ENTRYPOINT ["node-debug"]  

