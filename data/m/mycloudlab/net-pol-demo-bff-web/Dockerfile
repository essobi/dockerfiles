FROM node:8-alpine  
  
RUN mkdir /app  
  
# add source  
ADD . /app  
  
# add user apache  
RUN chown node:node /app -R  
  
RUN apk add --update openssl ca-certificates curl  
  
WORKDIR /app  
  
RUN yarn  
  
EXPOSE 3000  
# change user container  
USER node  
  
CMD [ "yarn","start" ]

