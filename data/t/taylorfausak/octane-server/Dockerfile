FROM node:6  
WORKDIR /code  
  
COPY . /code  
RUN npm install  
  
ENV HOST 0.0.0.0  
ENV PORT 80  
EXPOSE 80  
CMD node .  

