# Select source image  
FROM
node:wheezy@sha256:4e94d7eab2c3c8c59647b534699c32c5cbcdce371e70eb314c2d056922b2a2f1  
  
# Install all dependencies  
RUN apt-get update -q && apt-get upgrade -y --no-install-recommends  
  
# Create app directories  
RUN mkdir -p /usr/app  
WORKDIR /root  
  
# We download the opal interface  
RUN git clone -b master https://github.com/opal-project/opal-cache  
  
WORKDIR /root/opal-cache  
  
# Bundle app  
RUN cp package.json /usr/app/ \  
&& cp -r src /usr/app/src  
  
WORKDIR /usr/app  
  
# Install opal-interface npm dependencies  
RUN npm install --silent; exit 0;  
RUN cat /root/.npm/_logs/*; exit 0;  
  
# Run compute service  
EXPOSE 80  
CMD [ "npm", "start" ]  

