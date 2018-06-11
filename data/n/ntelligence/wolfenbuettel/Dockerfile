FROM loicmahieu/alpine-nginx-node  
  
MAINTAINER Andreas Helmberger <public@ahelmberger.de>  
  
ENV VIRTUAL_HOST wb-app.ahelmberger.de  
  
COPY package.json /sources/package.json  
COPY npm-shrinkwrap.json /sources/npm-shrinkwrap.json  
  
WORKDIR /sources  
  
RUN npm config set maxsockets 5  
RUN npm install  
  
COPY . /sources  
  
RUN npm run build-int && \  
mkdir /html && \  
mv -v ./dist/* /html && \  
mv -v ./nginx.conf /etc/nginx/conf/nginx.conf && \  
rm -rf /sources  

