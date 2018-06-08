FROM node:alpine  
  
# Install app  
RUN mkdir -p /app/files  
WORKDIR /app  
COPY . .  
RUN npm install --production  
  
ENV NODE_ENV production  
  
# Default settings  
ENV SERVE_CORS 1  
ENV SERVE_TREELESS 0  
# Default credentials  
ENV SERVE_USER user  
ENV SERVE_PASSWORD password  
  
# Expose port and volume  
EXPOSE 443  
VOLUME /app/files  
  
CMD npm start  

