FROM alpine:3.5  
RUN apk add --no-cache docker nodejs bash findutils libewf  
  
RUN echo '{ "allow_root": true }' > /root/.bowerrc  
  
COPY ./ /root/ipedqueue/  
WORKDIR /root/ipedqueue/  
  
RUN npm install --only=production  
  
CMD ["npm", "start"]  

