FROM node:7.10.0-alpine  
  
ENV NODE_ENV production  
ENV JENKINS_SERVERS http://localhost:8080/jenkins  
  
WORKDIR /app  
  
ADD package.json bower.json /app/  
  
RUN apk add --no-cache git zlib-dev lcms2-dev \  
libpng-dev \  
gcc \  
g++ \  
make \  
autoconf \  
automake && \  
npm install -g gulp bower && \  
npm install && \  
bower install --allow-root  
  
ADD . /app  
RUN gulp build  
  
EXPOSE 9000  
CMD gulp serve:prod  

