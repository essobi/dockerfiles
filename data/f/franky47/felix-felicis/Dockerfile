FROM node:7.7-alpine  
  
LABEL maintainer="Francois Best <francoisbest@gmail.com>"  
  
# Expose API ports  
EXPOSE 3000  
ENV PORT=3000 NODE_ENV=production LOGS_DIR=.logs  
  
# Create working dir and move stuff there  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
# Install dependencies  
COPY ./package.json /usr/src/app  
RUN npm install --production --silent  
  
# Install business code  
COPY src /usr/src/app/src  
  
VOLUME ["/usr/src/app/.logs"]  
  
# Launch !  
CMD ["node", "./src/index.js"]  

