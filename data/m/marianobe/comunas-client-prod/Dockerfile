FROM node:6  
EXPOSE 3001 3002  
  
RUN apt-get update && apt-get install nginx -y  
COPY nginx/default /etc/nginx/sites-available/default  
COPY nginx/nginx.conf /etc/nginx/nginx.conf  
  
RUN mkdir -p /root/.config/configstore  
RUN chmod 777 /root /root/.config /root/.config/configstore  
#ADD insight-yo.json /root/.config/configstore  
RUN npm install -g gulp-cli webpack yo generator-fountain-webapp generator-
fountain-angular1  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
ADD package.json /tmp/package.json  
RUN cd /tmp && npm install  
  
ADD . /usr/src/app  
RUN ln -sf /tmp/node_modules /usr/src/app/node_modules  
RUN npm run build  
  
CMD nginx  

