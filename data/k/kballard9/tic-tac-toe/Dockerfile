FROM nodesource/centos7:5.9.1  
RUN npm set strict-ssl false  
ENV NODE_ENV dev  
ADD package.json package.json  
RUN npm install  
COPY . .  
EXPOSE 3000  
CMD ["npm", "run", "dev"]

