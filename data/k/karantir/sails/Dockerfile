FROM alpine:3.5  
MAINTAINER Dmitry Krupnov <dmitry.krupnov@gmail.com>  
  
RUN apk add \--no-cache nodejs git  
RUN npm install -g sails bower mocha && npm cache clean  
  
ENV USER sails  
ENV PROJECT_ROOT /proj  
  
RUN adduser -D -u 1000 ${USER}  
USER ${USER}  
WORKDIR ${PROJECT_ROOT}  
VOLUME ${PROJECT_ROOT}  
  
EXPOSE 1337  
  
CMD ["sails", "lift"]

