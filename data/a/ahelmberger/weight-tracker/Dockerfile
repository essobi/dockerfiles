FROM node:8.11.0-alpine AS base  
  
WORKDIR /app  
  
COPY . ./  
  
RUN yarn install && yarn run build && rm -rf node_modules/ && yarn install
--production  
  
# --------------------------------------------------------------------  
FROM node:8.11.0-alpine AS release  
  
WORKDIR /app  
  
COPY \--from=base /app/ ./  
  
ENV VIRTUAL_HOST wt.ahelmberger.de  
  
ENV PORT 80  
EXPOSE 80  
CMD ["node", "server/index.js"]  

