FROM node:alpine  
  
RUN npm install --global yarn \  
&& rm -Rf /tmp/* /root/.npm /root/.cache  
  
ENV APP_DIR /usr/src/app  
RUN mkdir -p $APP_DIR  
WORKDIR $APP_DIR  

