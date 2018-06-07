FROM node:6  
COPY package.json /ls-ui/ui/dashboard/package.json  
WORKDIR /ls-ui/ui/dashboard/  
RUN npm install --production  
  
COPY src/ /ls-ui/ui/dashboard/src  
COPY public/ /ls-ui/ui/dashboard/public  
  
RUN npm run prod  
  
RUN mv /ls-ui/ui/dashboard/public /tmp/dashboard  
RUN rm -rf /ls-ui/ui/dashboard/  
RUN mv /tmp/dashboard /ls-ui/ui/  
  
VOLUME /ls-ui/ui/dashboard  
  
CMD ["echo", "'ls-ui file volume mounted over /ls-ui/'"]  

