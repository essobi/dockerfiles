FROM node:latest  
WORKDIR /app  
COPY . /app/  
RUN npm i npm@latest -g  
RUN npm install -g @angular/cli@latest --unsafe-perm  
RUN npm install --unsafe-perm  
ENTRYPOINT ["ng","serve","--host","0.0.0.0","--port","8081"]  
EXPOSE 8081  

