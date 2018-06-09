FROM node:8  
MAINTAINER Christian Metz <christian@metzweb.net>  
  
ENV SWAGGER_UI_VERSION 3.2.2  
ENV SWAGGER_SPEC_PATH /swaggerui/swagger/  
  
# Create app directories and install unzip  
RUN mkdir -p /usr/src/app && \  
mkdir -p /swaggerui/swagger && \  
apt-get update && \  
apt-get install -y unzip  
  
WORKDIR /swaggerui  
  
# Download Swagger UI  
ADD https://github.com/swagger-api/swagger-
ui/archive/v${SWAGGER_UI_VERSION}.zip /swaggerui/${SWAGGER_UI_VERSION}.zip  
COPY src/swagger.json /swaggerui/swagger/swagger.json  
  
# Unzip Swagger archive, copy dist files, and change the default endpoint  
# from petstore to the local API  
RUN unzip ${SWAGGER_UI_VERSION}.zip && \  
rm ${SWAGGER_UI_VERSION}.zip && \  
mv swagger-ui-${SWAGGER_UI_VERSION}/dist/* . && \  
rm -r swagger-ui-${SWAGGER_UI_VERSION}/ && \  
sed -i "s|http://petstore.swagger.io/v2/swagger.json|/spec|g" index.html  
  
WORKDIR /usr/src/app  
  
# Install app dependencies  
COPY src/package.json .  
RUN npm install  
  
# Bundle app source  
COPY src/server.js .  
  
EXPOSE 8080  
CMD ["npm", "start"]  

