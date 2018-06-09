FROM node:6  
WORKDIR /timelapse-ui  
COPY package.json package.json  
RUN npm install  
  
COPY src/ src/  
COPY public/ public/  
  
RUN npm run build  
  
RUN mkdir /ls-ui/  
RUN mkdir /ls-ui/ui/  
RUN mv build /ls-ui/ui/timelapse  
  
VOLUME /ls-ui/ui/timelapse  
  
CMD ["echo", "'timelapse-ui file volume mounted over /ls-ui/'"]  

