FROM node:5  
MAINTAINER Kazumichi Yamamoto <yamamoto.febc@gmail.com>  
  
RUN mkdir -p /gitbook  
WORKDIR /gitbook  
COPY ./app/package.json /gitbook/  
RUN npm install  
RUN $(npm bin)/gitbook help  
  
ENV PATH $PATH:/gitbook/node_modules/.bin  
WORKDIR /gitbook/app  
  
ENTRYPOINT ["npm"]  
CMD ["start"]  
EXPOSE 4000  

