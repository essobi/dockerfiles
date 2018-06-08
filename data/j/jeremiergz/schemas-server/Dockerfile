FROM node:8.11.1-alpine AS builder  
  
WORKDIR /app  
COPY . .  
  
RUN npm install && \  
npm run build && \  
npm prune --production && \  
mkdir package && \  
mv LICENSE README.md package.json dist/ node_modules/ package/  
  
FROM node:8.11.1-alpine AS runner  
  
LABEL maintainer="Jeremie Rodriguez <contact@jeremierodriguez.com>
(https://github.com/jeremiergz)" \  
description="Small server serving JSON schema files."  
  
ENV NODE_ENV=production  
  
WORKDIR /app  
COPY \--from=builder /app/package/ ./  
  
EXPOSE 20999  
CMD ["npm", "start"]  

