FROM node:8-alpine  
  
RUN mkdir /app  
  
# add source  
ADD . /app  
  
# add user apache  
RUN chown node:node /app -R  
  
WORKDIR /app  
  
RUN yarn && chmod 777 /app -R  
  
RUN apk add --update openssl ca-certificates curl  
  
EXPOSE 4200  
# change user container  
USER node  
  
CMD [ "yarn","start" ]

