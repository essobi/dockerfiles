FROM node:latest  
  
ENV NODE_ENV=production  
  
ADD package.json /tmp/package.json  
  
RUN cd /tmp && yarn  
  
RUN mkdir -p /idrak/server && cp -a /tmp/node_modules /idrak/server/  
  
WORKDIR /idrak/server  
  
ADD . /idrak/server  
  
# Uncomment to insert admin and languages.  
#ENV READER_INIT=true  
  
EXPOSE 3000  
  
CMD ["npm", "start"]  

