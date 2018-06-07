FROM node:8.11.2-alpine  
  
RUN mkdir /app  
  
ADD . /app  
  
WORKDIR app  
  
EXPOSE 8080  
ENV NPM_CONFIG_LOGLEVEL warn  
  
RUN npm install && npm install app --save font-awesome angular2-fontawesome &&
npm install http-server -g  
  
RUN node_modules/.bin/ng build --prod --output-path=../dist  
  
RUN ls  
  
WORKDIR ..  
  
#RUN rm -rf app  
CMD http-server dist

