FROM node:9.4.0  
LABEL author="gregossito"  
  
ENV NODE_ROOT /var/www  
  
WORKDIR $NODE_ROOT  
  
COPY . .  
  
RUN npm cache verify \  
&& npm install node-sass@4.7.2 --force \  
&& npm install webpack@3.10.0 \  
&& npm install webpack-dev-server@2.9.5 \  
&& npm install --force  
  
EXPOSE 8080  
CMD ["npm", "run", "build"]  

