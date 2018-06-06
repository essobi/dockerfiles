FROM node:6  
WORKDIR /code  
  
ADD . /code  
  
RUN npm install && \  
npm install -g http-server && \  
npm run build  
  
EXPOSE 9085  
ENTRYPOINT http-server /code/dist -p 9085 -a 0.0.0.0  

