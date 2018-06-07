FROM node:8-alpine  
  
WORKDIR /swagger  
RUN yarn global add yaml-include  
  
COPY ./build.js /build.js  
  
CMD [ "openapi.yml" ]  
  
ENTRYPOINT [ "node", "/build.js" ]  

