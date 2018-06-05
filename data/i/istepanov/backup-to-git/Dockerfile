FROM istepanov/cron  
MAINTAINER Ilya Stepanov <dev@ilyastepanov.com>  
  
RUN apk add --no-cache git ca-certificates  
  
RUN mkdir -p /target  
  
ENV GIT_BRANCH 'master'  
ENV GIT_COMMIT_MESSAGE 'Automatic backup'  
ENV TARGET_FOLDER '/target'  

