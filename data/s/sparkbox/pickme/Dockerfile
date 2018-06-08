FROM node:4-slim  
  
ENV src /var/pickme/  
ENV PORT 80  
# Move the package.json file over only so we can cache node_modules between  
# source changes  
COPY package.json ${src}  
  
WORKDIR ${src}  
RUN ["npm", "install", "--production"]  
  
COPY . ${src}  
  
EXPOSE 80  
CMD ["npm", "start"]  

