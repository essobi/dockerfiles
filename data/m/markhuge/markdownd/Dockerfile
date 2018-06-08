# docker run -d \  
# -p 8090:8090 \  
# --name markdown \  
# markhuge/instant-markdown-d  
FROM node:latest  
  
MAINTAINER Mark Wilkerson <mark@markwilkerson.me>  
  
EXPOSE 8090  
RUN npm i -g instant-markdown-d  
  
ENTRYPOINT ["instant-markdown-d"]  

