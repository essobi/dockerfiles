FROM node:8.9.4  
# Copy source code  
COPY . /app  
  
# Change working directory  
WORKDIR /app  
  
# Install dependencies  
RUN npm i -g yarn \  
&& yarn install  
  
# Expose API port to the outside  
EXPOSE 8000  
# Launch application  
CMD ["yarn","start"]

