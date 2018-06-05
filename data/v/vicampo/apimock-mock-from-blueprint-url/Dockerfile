FROM node:7-alpine  
  
COPY . /app  
WORKDIR /app  
  
RUN apk add --update curl  
  
# Install app npm dependencies  
RUN npm i -g drakov  
  
EXPOSE 3000  
CMD [ "./downloadAndStart.sh" ]  

