# Setting the base to nodejs 8.9.4  
FROM
node:8.9.4-alpine@sha256:14b627a91c92566d489d9d9073e465563be0e0c598c9537aa32e871a812018f5  
  
#### Begin setup ####  
# Installs git  
RUN apk add --update --no-cache git  
  
# Bundle app source  
COPY . /src  
  
# Change working directory  
WORKDIR "/src"  
  
# Install dependencies  
RUN npm install --production  
  
ENV NODE_ENV production  
  
# Expose 3000  
EXPOSE 3000  
# Startup  
ENTRYPOINT npm start

