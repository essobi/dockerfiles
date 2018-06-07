FROM mhart/alpine-node:6  
RUN apk add --update --no-cache curl  
  
WORKDIR /code  
ADD files .  
RUN npm install  
  
EXPOSE 3000  
CMD ["npm", "start"]

