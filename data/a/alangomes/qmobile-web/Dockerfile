FROM node:8-alpine  
  
RUN apk add --no-cache curl  
  
COPY package*.json ./  
  
RUN npm set progress=false && npm config set depth 0 && npm cache clean
--force  
  
WORKDIR /app-src  
  
COPY . .  
  
RUN npm i && \  
npm run build:ssr && \  
mkdir -p /app && \  
cd /app && \  
cp -r /app-src/dist /app/dist && \  
rm -rf /app-src  
  
WORKDIR /app  
  
ENV PORT=80  
EXPOSE 80  
HEALTHCHECK \--interval=30s --timeout=5s --retries=5 CMD curl --fail
http://localhost || exit 1  
  
CMD ["node", "dist/server"]  

