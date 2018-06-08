FROM node:8.0.0-alpine  
  
RUN addgroup -S nodejs && adduser -S -g nodejs nodejs  
RUN apk add --no-cache bash sed git openssh  
  
RUN cd /tmp && git clone -b development
https://github.com/jvwong/navigator.git  
RUN cd /tmp/navigator && npm install  
RUN npm install -g webpack http-server  
  
RUN mkdir -p /webapps/navigator  
WORKDIR /webapps/navigator  
  
RUN cp -r /tmp/navigator/. /webapps/navigator/  
  
# replace www host to beta in development  
RUN npm run build  
  
RUN chown -R nodejs:nodejs /webapps/navigator  
  
EXPOSE 8080  
USER nodejs  
  
CMD ["http-server", "./public", "-p", "8080"]  

