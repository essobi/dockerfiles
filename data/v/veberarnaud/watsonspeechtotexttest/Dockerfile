FROM node:6.3.0-slim  
  
MAINTAINER VEBER Arnaud  
  
ENV APP_SOURCE /usr/src/app  
  
# apt dependencies  
RUN apt-get update \  
&& apt-get install -y libav-tools \  
&& rm -rf /var/lib/apt/lists/*  
  
# ghost source  
RUN mkdir -p $APP_SOURCE  
WORKDIR $APP_SOURCE  
  
# npm dependencies  
COPY package.json package.json  
RUN npm install --loglevel warn \  
&& npm cache clean \  
&& rm -rf /tmp/npm*  
  
# sources  
COPY . $APP_SOURCE  
  
EXPOSE 3000  
CMD ["npm", "start"]  

