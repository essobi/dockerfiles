FROM node:8.6.0  
#===============================#  
# Docker Image Configuration #  
#===============================#  
LABEL Description="PMKB Bot" \  
Vendor="Englander Institute for Precision Medicine" \  
maintainer="als2076@med.cornell.edu"  
WORKDIR /usr/src/app  
#===================================#  
# Install PMKB Bot Dependencies #  
#===================================#  
COPY package.json /usr/src/app/  
RUN npm install  
# Bundle app source  
COPY . /usr/src/app  
#===================================#  
# Startup #  
#===================================#  
EXPOSE 3978  
CMD [ “npm”, “start” ]

