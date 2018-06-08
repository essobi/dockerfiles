FROM mhart/alpine-node:6  
EXPOSE 80  
RUN apk update && \  
apk upgrade && \  
apk add --no-cache bash git  
  
ARG YENV=production  
ARG YANDEX_ENVIRONMENT=production  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
ADD https://github.com/bem-site/bem-forum-content-ru/raw/master/archive.json
./archive_ru.json  
ADD https://github.com/bem-site/bem-forum-content-en/raw/master/archive.json
./archive_en.json  
  
# install dependencies  
COPY package.json /usr/src/app/  
  
RUN git init \  
&& npm install --production=false \--quiet  
  
# install project  
COPY . /usr/src/app  
  
RUN YENV=production npm run make \  
&& npm prune --production \  
&& rm -rf .git  
  
CMD node server  

