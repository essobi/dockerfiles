FROM mhart/alpine-node:8  
  
WORKDIR /project  
  
# Add node_modules/.bin to PATH  
ENV PATH /project/node_modules/.bin:$PATH  
RUN apk update && apk upgrade && \  
apk add \--no-cache bash curl git openssh tzdata openssl su-exec  
  
RUN adduser -h /project -S nodejs && \  
addgroup -S nodejs && \  
addgroup nodejs nodejs  
  
CMD ["su-exec", "nodejs", "npm", "start", "-s", "--"]  
  

