FROM nlepage/codyglot:base as origin  
  
FROM node:9-alpine  
  
COPY \--from=origin /usr/local/bin/codyglot /usr/local/bin/codyglot  
  
ENTRYPOINT ["codyglot", "executor", "nodejs"]  

