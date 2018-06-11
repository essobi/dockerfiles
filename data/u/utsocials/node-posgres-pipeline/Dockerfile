FROM node:6.6  
# To use it locally and in bitbucket pipeline  
# download and install packages  
RUN apt-get update \  
&& apt-get install -y postgresql postgresql-contrib \  
&& apt-get install sudo \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
#create app and work dir  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
# Install app node dep  
COPY package.json /usr/src/app/  
RUN npm install  
RUN npm install pg  
  
# bundle app source  
COPY . /usr/src/app  
  

