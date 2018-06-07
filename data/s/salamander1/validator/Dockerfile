FROM node:9.11.1-alpine  
RUN apk add --no-cache git openjdk8  
RUN git clone https://github.com/veto64/validator  
WORKDIR validator  
RUN npm i  
RUN npm i -g forever  
EXPOSE 4000  
CMD [ "npm", "start" ]  
#ENTRYPOINT [""]  

