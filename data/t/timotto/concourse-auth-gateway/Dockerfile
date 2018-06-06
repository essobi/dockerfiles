FROM node:8-alpine AS build  
  
ADD . /build  
  
WORKDIR /build  
  
RUN npm install -g yarn && \  
yarn install && \  
yarn run test && \  
yarn run tsc && \  
rm -rf node_modules/ && \  
yarn install \--production=true  
FROM node:8-alpine AS runtime  
  
COPY \--from=build /build /app  
  
WORKDIR /app  
  
ENV PORT 3001  
  
ENV STATE_FILENAME /state.json  
  
CMD node dist

