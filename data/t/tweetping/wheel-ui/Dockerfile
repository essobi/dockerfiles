FROM node:6  
WORKDIR /matrix-ui  
COPY package.json package.json  
RUN npm install  
  
COPY src/ src/  
COPY public/ public/  
  
RUN npm run build  
  
RUN mkdir /ls-ui/  
RUN mkdir /ls-ui/ui/  
RUN mv build /ls-ui/ui/matrix  
  
VOLUME /ls-ui/ui/matrix  
  
CMD ["echo", "'matrix-ui file volume mounted over /ls-ui/'"]  

