FROM node:7.10.1-alpine  
MAINTAINER Derek Brown <derek@allderek.com>  
  
# Create Directories  
# Install Source  
RUN apk update && \  
apk add git  
  
# Copy Source  
COPY ./src/ /usr/src/app/  
  
WORKDIR /usr/src/app/  
  
# Install App  
RUN mkdir -p /usr/lib/tuxlab/ssl/ && \  
npm install --production  
  
EXPOSE 22 80 443  
ENTRYPOINT ["npm"]  
CMD ["start"]  

