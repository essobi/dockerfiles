FROM node:9 AS build  
  
WORKDIR /build  
  
ADD yarn.lock .  
ADD package.json .  
ADD tsconfig.json .  
RUN yarn install  
  
ADD ./src ./src  
RUN yarn build:linux  
  
FROM debian  
  
COPY \--from=build /build/rotator /usr/bin/rotator  
RUN chmod +x /usr/bin/rotator  
  
CMD /usr/bin/rotator

