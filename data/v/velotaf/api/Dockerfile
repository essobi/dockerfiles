FROM node:8.9.1-alpine  
  
LABEL \  
AUTHOR='Francois Best <francoisbest@gmail.com>' \  
LICENSE='MIT' \  
REPOSITORY='https://github.com/velotaf/api'  
  
# Expose API ports  
EXPOSE 3000  
ENV \  
PORT=3000 \  
NODE_ENV=production \  
LOGS_DIR=.logs  
  
# Create working dir  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
# Install dependencies  
COPY ./package.json ./yarn.lock /usr/src/app/  
RUN apk --update add --no-cache yarn \  
&& yarn install --production \  
&& apk del yarn \  
&& rm -rf /var/cache/apk/*  
  
# Install business code  
COPY ./src /usr/src/app/src  
  
VOLUME ["/usr/src/app/.logs"]  
  
# Launch !  
CMD ["node", "./src/index.js"]  

