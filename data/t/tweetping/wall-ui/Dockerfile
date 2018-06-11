FROM node:6  
WORKDIR /wall-ui  
COPY package.json package.json  
RUN npm install  
  
ENV NODE_ENV production  
  
COPY app/ app/  
COPY public/ public/  
  
RUN npm run build  
  
RUN mkdir -p /ls-ui/ui/  
RUN mv public /ls-ui/ui/wall  
  
VOLUME /ls-ui/ui/wall  
  
CMD ["echo", "'wall-ui file volume mounted over /ls-ui/'"]

