FROM node  
WORKDIR /app  
COPY package.json .  
# when one would change pachage.json, it will rebuild layer below  
RUN npm install  
# when one would change index.s, it will rebuild layer below  
# it will not rebuild install dependencies layer  
COPY index.js .  
EXPOSE 3000  
CMD node index.js

