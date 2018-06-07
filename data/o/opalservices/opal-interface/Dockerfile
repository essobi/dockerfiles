# Select source image  
FROM node:wheezy  
  
# Install all dependencies  
RUN apt-get update -q && apt-get upgrade -y --no-install-recommends  
  
# Create app directories  
RUN mkdir -p /usr/app/config  
WORKDIR /root  
  
# We download the opal interface  
RUN git clone -b master https://github.com/opal-project/opal-interface  
  
WORKDIR /root/opal-interface  
  
# Bundle app  
RUN cp package.json /usr/app/ \  
&& cp -r src /usr/app/src \  
&& cp -r algorithms /usr/app/algorithms  
  
WORKDIR /usr/app  
  
# We create the audit directory  
RUN mkdir -p /usr/app/audit  
  
# Install opal-interface npm dependencies  
RUN npm install --silent; exit 0;  
RUN cat /root/.npm/_logs/*; exit 0;  
  
# Run interface service  
EXPOSE 80  
CMD [ "npm", "start" ]  

