FROM node:slim  
  
#########################  
# CONFIG SYSTEM #  
#########################  
  
# Create User with limited privilege  
RUN useradd --user-group --create-home --shell /bin/false app  
ENV HOME=/home/app  
  
USER app  
WORKDIR $HOME  
  
#########################  
# CONFIG APP #  
#########################  
  
# Install app dependencies  
COPY package.json $HOME  
RUN npm install  
  
# Copy source app  
COPY . $HOME  
  
# Expose port  
EXPOSE 8080

