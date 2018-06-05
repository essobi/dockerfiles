FROM node:6.6.0-slim  
  
LABEL Description="A docker wallboard" Version="0.0.1" Name="Behold"  
  
ENV PORT 80  
ENV NODE_ENV production  
  
EXPOSE 80  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
COPY . /usr/src/app  
  
CMD [ "npm", "start" ]  

