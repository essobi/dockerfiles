FROM node:latest  
MAINTAINER Logan Sparlin <lsparlin@marlinco.com>  
  
# ENV MONGO_URL
mongodb://marlindev:305Millst@candidate.54.mongolayer.com:10724,candidate.33.mongolayer.com:11033/cobb-
guides-dev?replicaSet=set-56439d4e5ee2011db80007d4  
# ENV PORT 5000  
# ENV SECRET 98720hgj18930y908hgj03984ht9-81j34ijf9038qg  
# ENV s3AccessKeyId AKIAJ4R2OPWFPSDXLQKA  
# ENV s3SecretAccessKey 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  
# Create app directory  
RUN mkdir -p /src/api  
WORKDIR /src/api  
  
# make sure apt is up to date  
RUN apt-get update  
  
# Install deps  
COPY package.json /src/api  
RUN npm install  
  
# Bundle source  
COPY . /src/api  
  
EXPOSE 5000  
CMD ["npm", "start"]  

