FROM node:argon  
  
# Create src folder for app code  
RUN mkdir /src  
  
# Copy application code into container  
COPY . /src  
  
WORKDIR /src  
  
# Install application dependecies  
RUN npm install  
  
# Expose applcation port  
EXPOSE 3000  
# Start the application  
CMD ["npm","start"]  

