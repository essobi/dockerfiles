FROM node:9-alpine  
  
ARG VERSION  
RUN npm install -g junit-viewer@$VERSION  
  
VOLUME /results  
CMD ["junit-viewer", "--results=/results"]  

