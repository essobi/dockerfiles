FROM node:alpine  
LABEL maintainer="caspar.bauer0@gmail.com"  
LABEL name="recordings"  
LABEL version="1.0.1"  
  
# Add alternative repos since alpine ones seem to 503 from time to time  
RUN echo http://mirror.yandex.ru/mirrors/alpine/v3.6/main >
/etc/apk/repositories; \  
echo http://mirror.yandex.ru/mirrors/alpine/v3.6/community >>
/etc/apk/repositories  
  
# Install yarn (NOTE: we need python to build snappy, a compression library by
google for kafka)  
RUN apk update && apk add yarn python && rm -rf /var/cache/apk/*  
  
# Create workingdir  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
# Copy over the source code and build it  
COPY . /usr/src/app  
RUN yarn install && yarn run build  
  
EXPOSE 3000  
ENTRYPOINT yarn run start  

