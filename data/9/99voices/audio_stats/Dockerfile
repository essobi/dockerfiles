FROM node:alpine  
LABEL maintainer="caspar.bauer0@gmail.com"  
LABEL name="audio_stats"  
LABEL version="1.0.2"  
  
# Add alternative repos since alpine ones seem to 503 from time to time  
RUN echo http://mirror.yandex.ru/mirrors/alpine/v3.6/main >
/etc/apk/repositories; \  
echo http://mirror.yandex.ru/mirrors/alpine/v3.6/community >>
/etc/apk/repositories  
  
# Install yarn and sox  
RUN apk update && apk add yarn sox python && rm -rf /var/cache/apk/*  
  
# Create workingdir  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
# Copy over the source code and build it  
COPY . /usr/src/app  
RUN yarn install && yarn run build  
  
EXPOSE 3000  
ENTRYPOINT yarn run start  

