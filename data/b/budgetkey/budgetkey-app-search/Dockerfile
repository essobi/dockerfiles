FROM node:8-alpine  
  
COPY . /app/  
RUN apk add --update git  
  
# ENV NODE_ENV=production  
RUN cd /app/ && \  
npm install && \  
# uncomment the following line to enable integration with custom budgetkey-
ng2-components  
# you need to have a copy of budgetkey-ng2-components under .budgetkey-
ng2-compoments  
# cd .budgetkey-ng2-components && npm install --dev && npm run prebuild && npm
run prepublish && npm run install-into /app && cd .. &&\  
npm run dist  
  
EXPOSE 8000  
CMD cd /app/ && npm start  

