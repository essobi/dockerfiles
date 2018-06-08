FROM mhart/alpine-node:latest  
  
WORKDIR /opt/hub2slack  
ADD . .  
  
RUN npm install  
  
EXPOSE 80  
EXPOSE 443  
CMD ["npm", "start"]  

