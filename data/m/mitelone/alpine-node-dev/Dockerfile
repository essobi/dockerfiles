# npm & yarn included  
FROM mhart/alpine-node:8.9.4  
  
# If you have native dependencies, you'll need extra tools  
# As of Alpine Linux 3.3 there exists a new --no-cache option for apk.  
# It allows users to install packages with an index that is updated and  
# used on-the-fly and not cached locally  
RUN apk add \--no-cache make gcc g++ python git curl jq  

