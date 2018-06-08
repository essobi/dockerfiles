FROM node:4  
RUN mkdir /pleasebeer-front  
ADD ./ /pleasebeer-front/  
WORKDIR /pleasebeer-front  
RUN npm install --no-optional  
EXPOSE 80  
ENTRYPOINT ["npm", "start"]

