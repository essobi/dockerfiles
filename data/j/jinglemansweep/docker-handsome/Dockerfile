FROM node:alpine  
  
ARG handsome_url="https://github.com/davefp/handsome.git"  
RUN apk update && \  
apk add build-base git python && \  
git clone ${handsome_url} /opt/app && \  
cp -r /opt/app /opt/src && \  
cd /opt/app/ && \  
npm install  
  
EXPOSE 3000  
VOLUME ["/opt/app/dashboards", "/opt/app/jobs", "/opt/app/styles",
"/opt/app/views", "/opt/app/widgets"]  
  
WORKDIR /opt/app  
CMD ["npm", "start"]  
  

