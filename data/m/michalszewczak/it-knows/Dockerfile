FROM schmich/armv7hf-alpine-qemu  
  
COPY . .  
  
RUN ["cross-build-start"]  
  
RUN apk update && apk add nodejs && npm install && npm run build  
  
RUN ["cross-build-end"]  
  
CMD ["npm", "start"]  

