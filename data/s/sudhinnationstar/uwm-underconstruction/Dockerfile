FROM node:carbon  
RUN mkdir -p /uwm/images  
WORKDIR /uwm/underconstruction  
COPY *.* ./  
COPY images/*.png ./images/  
RUN npm install  
EXPOSE 8080  
ENTRYPOINT ["npm", "start"]

