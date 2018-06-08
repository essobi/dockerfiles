FROM node:5.7  
  
EXPOSE 80  
  
WORKDIR /home/nld-web/  
  
ADD package.json /home/nld-web/  
RUN npm install  
  
ARG BUILD_ENV  
  
ADD apple-touch-icon.png /home/nld-web/  
ADD android-touch-icon.png /home/nld-web/  
ADD placeholder.png /home/nld-web/  
ADD index.html /home/nld-web/  
  
ADD server /home/nld-web/server  
  
ADD tsconfig.json /home/nld-web/  
ADD typings.json /home/nld-web/  
  
ADD app/ /home/nld-web/app/  
RUN npm run tsc; exit 0  
RUN npm run pick-config  
  
CMD ["npm", "run", "serve"]  

