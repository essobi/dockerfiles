###########################################################  
#  
# Dockerfile for laurentius  
#  
###########################################################  
  
# Setting the base to nodejs 4.3.1  
FROM mhart/alpine-
node:4.9.1@sha256:052772af605978749631e2b6d190c7d68dc607a480a6e4dbe84eaf7264759d2e  
  
# Maintainer  
MAINTAINER Jonas Enge  
  
#### Begin setup ####  
  
# Installs git  
RUN apk add --update git && rm -rf /var/cache/apk/*  
  
# Bundle app source  
COPY . /src  
  
# Change working directory  
WORKDIR "/src"  
  
# Install dependencies  
RUN npm install --production  
  
# Env variables  
ENV TFK_LAURENTIUS_JWT_KEY NeverShareYourSecret  
ENV TFK_LAURENTIUS_CALLBACK_STATUS_MESSAGE Varselbrev arkivert  
ENV TFK_LAURENTIUS_ARCHIVE_JOB_DIRECTORY_PATH test/data/archive/jobs  
ENV TFK_LAURENTIUS_ARCHIVE_DONE_DIRECTORY_PATH test/data/archive/done  
ENV TFK_LAURENTIUS_ARCHIVE_ERROR_DIRECTORY_PATH test/data/archive/errors  
ENV TFK_LAURENTIUS_P360WS_USER domain/username  
ENV TFK_LAURENTIUS_P360WS_PASSWORD password  
ENV TFK_LAURENTIUS_P360WS_BASEURL http://tfk-fh-
siweb01t.login.top.no:8088/SI.WS.Core/SIF/  
  
# Startup  
ENTRYPOINT node example.js  

