##  
# ------- Build image  
##  
FROM node:8.11.1 AS build  
  
WORKDIR /opt/build  
  
# Copy app sources  
COPY . .  
  
# Install node dependencies  
RUN npm install  
  
# Build source code  
RUN npx gulp  
  
##  
# -------- Release image  
##  
FROM nginx:1.13.11-alpine AS release  
  
COPY \--from=build /opt/build/server/default.conf
/etc/nginx/conf.d/default.conf  
COPY \--from=build /opt/build/public /usr/share/nginx/html

