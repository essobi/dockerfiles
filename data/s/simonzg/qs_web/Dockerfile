FROM nginx:1.12.1-alpine  
  
RUN mkdir /app  
COPY . /app  
WORKDIR /app  
  
RUN apk --update add nodejs && \  
npm install -g npm && \  
npm install && \  
API_HOST="CURRENT" npm run build && \  
rm -rf src .git node_modules \  
rm -rf /var/cache/apk/* && \  
npm uninstall npm -g && \  
apk del nodejs  
  
COPY ./conf/stage.default.conf /etc/nginx/conf.d/default.conf  

