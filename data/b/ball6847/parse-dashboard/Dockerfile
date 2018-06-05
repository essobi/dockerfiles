FROM node:7-alpine  
MAINTAINER Porawit Poboonma <ball6847@gmail.com>  
  
# ENVIRONMENT VARIABLE SUPPORTED BY PARSE DASHBOARD  
ENV TERM=xterm-256colors \  
HOST=0.0.0.0 \  
PORT=4040 \  
MOUNT_PATH=/ \  
PARSE_DASHBOARD_ALLOW_INSECURE_HTTP= \  
PARSE_DASHBOARD_TRUST_PROXY= \  
PARSE_DASHBOARD_SERVER_URL= \  
PARSE_DASHBOARD_MASTER_KEY= \  
PARSE_DASHBOARD_APP_ID= \  
PARSE_DASHBOARD_APP_NAME= \  
PARSE_DASHBOARD_USER_ID= \  
PARSE_DASHBOARD_USER_PASSWORD= \  
PARSE_DASHBOARD_SSL_KEY= \  
PARSE_DASHBOARD_SSL_CERT= \  
PARSE_DASHBOARD_CONFIG=  
  
# see https://github.com/ParsePlatform/parse-dashboard/blob/master/Parse-
Dashboard/index.js for reference  
  
RUN npm install -g parse-dashboard@1.0.25  
  
EXPOSE 4040  
  
ENTRYPOINT [ "parse-dashboard" ]  

