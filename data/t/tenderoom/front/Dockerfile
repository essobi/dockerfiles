FROM kelecorix/stack-nodejs-build-lumper:latest  
MAINTAINER sigrlami <sergey.bushnyak@sigrlami.eu>  
  
WORKDIR /app/frontend  
COPY ./src ./src  
COPY ./webpack ./webpack  
COPY ["package.json", "tsconfig.json", "tslint.json", "npm-shrinkwrap.json",
"./"]  
  
RUN npm install  
RUN npm run build:dev  
  
WORKDIR /app  
COPY ./docker-entrypoint.sh ./  
RUN chmod 775 /app/docker-entrypoint.sh  
  
ENTRYPOINT ["/app/docker-entrypoint.sh"]  
WORKDIR /app/  
CMD run

