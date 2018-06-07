FROM node:8-alpine  
  
ENV NODE_API_URI=http://localhost:14700  
RUN npm i -g iota-pm  
COPY docker-entrypoint.sh /docker-entrypoint.sh  
RUN chmod +x /docker-entrypoint.sh  
  
EXPOSE 8888  
ENTRYPOINT ["/docker-entrypoint.sh"]  

