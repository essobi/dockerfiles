FROM mhart/alpine-node:5.7.1  
MAINTAINER Corey Butler  
  
ENV LETSENCRYPT_CERT_ROOT /letsencrypt  
ENV AWS_S3_REGION us-east-1  
ADD ./app /app  
WORKDIR /app  
  
RUN apk add -U openssl && cd /app && npm i  
  
ENTRYPOINT ["npm", "start"]  

