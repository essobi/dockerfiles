FROM node:8-alpine as build  
  
RUN apk --no-cache --virtual .build add build-base python  
  
# taken from node:6-onbuild  
#RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
# copy in main package.json and yarn.lock  
COPY package.json /usr/src/app/  
COPY yarn.lock /usr/src/app/  
  
# npm rebuild is required because the prebuilt binaries are not compatible
with musl  
# remove when https://github.com/kelektiv/node.bcrypt.js/issues/528 is
resolved  
RUN yarn install --pure-lockfile --production \  
&& npm rebuild bcrypt --build-from-source  
  
COPY . /usr/src/app  
  
# Final stage  
FROM node:8-alpine  
  
WORKDIR /usr/src/app  
COPY \--from=build /usr/src/app /usr/src/app  
  
CMD [ "yarn", "start" ]  

