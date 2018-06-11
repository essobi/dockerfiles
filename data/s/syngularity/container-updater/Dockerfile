FROM mhart/alpine-node:6  
VOLUME /opt/app/run  
  
ARG CUPD_VERSION  
ENV CUPD_VERSION=${CUPD_VERSION:-"1.0.0"}  
  
LABEL syngularity.docker.updater="${CUPD_VERSION}"  
  
WORKDIR /opt/app  
COPY . ./  
RUN npm i --production=true \--quiet  
  
CMD npm start  

