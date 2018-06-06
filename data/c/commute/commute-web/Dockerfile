FROM mhart/alpine-node:6.2.2  
# FROM mhart/alpine-node:base-0.10  
# FROM mhart/alpine-node  
RUN apk --update add python make g++ libpng-dev bash build-base nasm autoconf
automake  
  
WORKDIR /app  
  
# Install and cache node_modules  
ADD package.json package.json  
  
RUN npm install  
  
ADD bin bin  
ADD build build  
ADD config config  
ADD server server  
ADD src src  
ADD tests tests  
  
ADD .eslintrc .eslintrc  
  
ENV NODE_ENV production  
  
RUN npm run deploy-docker:prod  
  
# If you have native dependencies, you'll need extra tools  
# RUN apk add --no-cache make gcc g++ python  
# If you need npm, don't use a base tag  
# RUN npm install  
  
EXPOSE 3000  
CMD ["node", "bin/server"]  

