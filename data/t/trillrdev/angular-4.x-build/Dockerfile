FROM node:6-alpine  
  
RUN npm i -g @angular/cli@latest \  
&& npm i -g yarn \  
&& yarn add --dev webpack  
  
CMD cd /app && yarn install &&ng build --target=production  

